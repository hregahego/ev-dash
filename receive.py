import can
import cantools
import can_utils
from time import time

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
except OSError as e:
    print(f"Error opening CAN bus: {e}")
    print("Ensure the CAN interface is up and configured (e.g., 'sudo ip link set can0 up type can bitrate 500000')")
    exit()

cache = {}
db = cantools.database.load_file('CONTROLS.dbc')
last_received = 0

import time

def get_message(message):
    global last_received, cache

    if time.time() - message.timestamp > 5:
        return None
    try:
        decoded = can_utils.decode_msg(db, message)
    except SystemExit as e:
        print("SystemExit triggered during CAN decode:", e)
        return None
    
    for sig, value in decoded.items():
        cache[sig] = [value, message.timestamp]

    last_received = message.timestamp
    return cache

def save_cache():
    global cache
    date = time.strftime("%m/%d")
    with open(f'logs/{date}.txt', 'w') as f:
        for sig, (value, timestamp) in cache.items():
            f.write(f"{sig}: {value} (last updated: {time.ctime(timestamp)})\n")

try:
    while True:
        print("Waiting for CAN messages...")
        message = bus.recv()
        if message:
            print(get_message(message))

except KeyboardInterrupt:
    bus.shutdown()
except Exception as e:
    bus.shutdown()
    print(e)


