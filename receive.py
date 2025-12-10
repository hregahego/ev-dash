import can
import cantools
import can_utils

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
except OSError as e:
    print(f"Error opening CAN bus: {e}")
    print("Ensure the CAN interface is up and configured (e.g., 'sudo ip link set can0 up type can bitrate 500000')")
    exit()

cache = {}
db = cantools.database.load_file('CONTROLS.dbc')

try:
    while True:
        message = bus.recv()
        if message:
            decoded = can_utils.decode_msg(db, message)
            for key in decoded.keys():
                cache[key] = decoded[key]
            print(cache)
except KeyboardInterrupt:
    bus.shutdown()
except Exception as e:
    bus.shutdown()
    print(e)

