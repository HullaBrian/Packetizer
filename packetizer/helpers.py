from __future__ import annotations
from dataclasses import dataclass

from loguru import logger


class Exceptions:
    class MalformedTemplate(Exception):
        pass

    class MalformedData(Exception):
        pass


def _check_packet_format(packet: list[str]):
    accepted_data_types = [
        "str",
        "int",
        "hex"
    ]
    try:
        for line_num, line in enumerate(packet):
            split_line = [field.replace("\n", "") for field in line.split(":")]
            assert len(split_line) == 3
            assert split_line[1] in accepted_data_types

            try:
                _ = int(split_line[-1])
            except ValueError:
                flag = False
                for back_trace in packet[0:line_num]:
                    if back_trace.split(":")[0] == split_line[-1]:
                        flag = True
                if not flag:
                    raise AssertionError

    except AssertionError:
        raise Exceptions.MalformedTemplate(f"Malformed template on line {line_num + 1} of template")


def _check_data_with_template(template: list[str], data: dict):
    try:
        for line in template:
            split_line = line.split(":")
            _ = data[split_line[0]]
    except KeyError:
        raise Exceptions.MalformedData(f"Could not find '{split_line[0]}' entry")


@dataclass
class PacketField:
    field_name: str
    data_type: str
    data_size: str | int
