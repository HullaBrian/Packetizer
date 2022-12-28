from packetizer import encode, decode


data = {
        "FIRST_FIELD": 100,
        "SECOND_FIELD": "TEST",
        "THIRD_FIELD_LENGTH": 4,
        "FOURTH_FIELD": "Yep",
        "FIFTH_FIELD": int('420', base=16)
}
encoded_packet = encode(template=open("example.packet", "r"), data=data)
