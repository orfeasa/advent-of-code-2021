from dataclasses import dataclass, field


@dataclass
class Packet:
    version: int = 0
    type_id: int = 0
    value: int = None
    subpackets: list = field(default_factory=list)


def parse_transmission(
    transmission: str, length=None, number_of_packets=None
) -> list[Packet]:
    if len(transmission) == 0:
        return []
    first_bit = 0
    packet = Packet()
    packet.version = int(transmission[first_bit : first_bit + 3], 2)
    packet.type_id = int(transmission[first_bit + 3 : first_bit + 6], 2)
    last_bit = first_bit + 6

    # literal
    if packet.type_id == 4:
        keep_reading = True
        number = ""
        while keep_reading:
            keep_reading = bool(int(transmission[last_bit : last_bit + 1]))
            number += transmission[last_bit + 1 : last_bit + 5]
            last_bit += 5
        packet.value = int(number, 2)
    else:
        length_type_id = int(transmission[last_bit : last_bit + 1])
        last_bit += 1
        if length_type_id == 0:
            total_length = int(transmission[last_bit : last_bit + 15], 2)
            last_bit += 15
            packet.subpackets = parse_transmission(
                transmission[last_bit : last_bit + total_length]
            )
            last_bit += total_length
        else:
            number_of_subpackets = int(transmission[last_bit : last_bit + 11], 2)
            last_bit += 11
            packet.subpackets = parse_transmission(
                transmission[last_bit:], number_of_packets=number_of_subpackets
            )
            if len(packet.subpackets) == number_of_subpackets:
                return [packet]

    if (
        len(transmission) == last_bit
        or transmission[last_bit:] == len(transmission[last_bit:]) * "0"
        # or length is not None and last_bit == length
    ):
        return [packet]
    return [packet] + parse_transmission(transmission[last_bit:])


def sum_version(packets: list) -> int:
    sum = 0
    for packet in packets:
        sum += packet.version if packet.version else 0
        sum += sum_version(packet.subpackets) if packet.subpackets else 0

    return sum


def part_one(filename: str) -> int:
    with open(filename) as f:
        transmission = f.read().strip()
    transmission = "620080001611562C8802118E34"
    transmission = str(bin(int(transmission, 16)))[2:].zfill(len(transmission) * 4)

    packets = parse_transmission(transmission)

    return sum_version(packets)


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_16/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
