from __future__ import annotations
import _io
import binascii

from loguru import logger

from packetizer.helpers import Exceptions
from packetizer.helpers import (
    _check_packet_format,
    _check_data_with_template,
    PacketField
)


def encode(template: str | _io.TextIOWrapper, data: bytes) -> bytes:
    if type(template) is not _io.TextIOWrapper:
        template = open(template, "r")

    lines = template.readlines()
    logger.info("Verifying data and template structure/format...")
    try:
        _check_packet_format(lines)
        _check_data_with_template(lines, data)
    except Exception as e:
        logger.critical("Something went wrong with verifying the integrity of the template/data!")
        return False
    logger.success("Verified data/template structure!")

    packet_template = {}
    for line in lines:
        split_line = line.split(":")
        packet_template[split_line[0]] = PacketField(
            split_line[0],
            split_line[1],
            split_line[2]
        )

    out: bytes = b""
    for field in data.keys():
        value = data[field]

        if type(value) is str and not value.startswith("0x"):
            out += bytes(value, "utf-8")
        elif type(value) is int:
            try:
                out += value.to_bytes(int(packet_template[field].data_size), 'big')
            except ValueError:
                out += value.to_bytes(int(data[field]), 'big')
        elif type(value) is str:  # hex value
            out += binascii.unhexlify(value.replace("0x", ""))

    return out


def decode(template: str | _io.TextIOWrapper, data: bytes) -> dict:
    pass
