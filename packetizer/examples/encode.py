from packetizer import encode


data = {
        "FIRST_FIELD": 100,
        "SECOND_FIELD": "TEST",
        "THIRD_FIELD_LENGTH": 20,
        "FOURTH_FIELD": "Yep",
        "FIFTH_FIELD": '0xfef00a01'
}
encoded_packet = encode(template=open("example.packet", "r"), data=data)
print(encoded_packet)