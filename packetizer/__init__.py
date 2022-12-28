from __future__ import annotations
import _io

from loguru import logger

from packetizer.helpers import (
    _check_packet_format,
    _check_data_with_template
)


def encode(template: str | _io.TextIOWrapper, data: bytes) -> bytes:
    if type(template) is not _io.TextIOWrapper:
        template = open(template)

    lines = template.readlines()
    logger.info("Verifying data and template structure/format...")
    try:
        _check_packet_format(lines)
        _check_data_with_template(lines, data)
    except Exception as e:
        logger.critical("Something went wrong with verifying the integrity of the template/data!")
        return False

    logger.success("Verified data/template structure!")

    for line in lines:
        pass


def decode(template: str | _io.TextIOWrapper, data: bytes) -> dict:
    pass
