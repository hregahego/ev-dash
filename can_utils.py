import cantools

dbc_path = ""

db = cantools.database.load_file(dbc_path);

def encode_msg(msg, data):
    msg = db.get_message_by_name(msg)
    encoded = msg.encode(data)
    return encoded

def decode_msg(msg, raw):
    msg = db.get_message_by_name(msg)
    decoded = msg.decode(raw)
    return decoded
