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

try:
    while True:
        message = bus.recv()
        if message:
            decoded = can_utils.decode_msg(message)
            print(decoded)
except:
    bus.shutdown()

