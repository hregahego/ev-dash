import can
import cantools
import can_utils

db = cantools.database.load_file('CONTROLS.dbc')

test_sigs = {"INV_Max_Discharge_Current": 10, "INV_Max_Charge_Current": 20}
msg_to_send = encode_msg(db, "BMS_Current_Limit", test_sigs)
