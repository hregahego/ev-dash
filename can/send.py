import can
import cantools
import can_utils

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan')
except OSError as e:
    print(f"Error opening CAN bus: {e}")
    print("Ensure the CAN interface is up and configured (e.g., 'sudo ip link set can0 up type can bitrate 500000')")
    exit()

db = cantools.database.load_file('CONTROLS.dbc')

test_sigs = {"INV_Max_Discharge_Current": 10, "INV_Max_Charge_Current": 20}
# msg_to_send = create_msg(db, "BMS_Current_Limit", test_sigs)
# 
# bus.send(msg_to_send)
encoded = can_utils.encode_msg(db, "BMS_Current_Limit", test_sigs)
print(encoded)
