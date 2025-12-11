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

def get_message(message):
    global last_received, cache

    if time.time() - message.timestamp > 5:
        return None
    decoded = can_utils.decode_msg(db, message)
    for key in decoded.keys():
        cache[key] = decoded[key]
    last_received = message.timestamp
    return cache 
    

try:
    while True:
        message = bus.recv()
        if message:
            print(get_message(message))
except KeyboardInterrupt:
    bus.shutdown()
except Exception as e:
    bus.shutdown()
    print(e)


