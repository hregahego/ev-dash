import cantools
import can
import sys

dbc_path = sys.argv[1]
db = cantools.database.load_file(dbc_path);

def encode_msg(db, msg_name, sig_values): #sig_values is a DICTIONARY
    msg = db.get_message_by_name(msg_name)
    encoded = msg.encode(sig_values)
    return encoded

def decode_msg(db, msg):
    decoded = db.decode_message(msg.arbitration_id, msg.data)
    return decoded


# if __name__ == "__main__":
#     test_sigs = {"INV_Max_Discharge_Current": 10, "INV_Max_Charge_Current": 20}
#     encoded_data = encode_msg(db, "BMS_Current_Limit", test_sigs)
#     decoded_data = decode_msg(db, "BMS_Current_Limit", encoded_data)
#     print(encoded_data)
#     print(decoded_data)

