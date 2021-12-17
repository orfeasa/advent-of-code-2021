def part_one(filename: str) -> int:
    with open(filename) as f:
        transmission = f.read().strip()
    transmission = "EE00D40C823060"
    transmission = str(bin(int(transmission, 16)))[2:].zfill(len(transmission) * 4)

    first_bit = 0
    version = int(transmission[first_bit : first_bit + 3], 2)
    type_id = int(transmission[first_bit + 3 : first_bit + 6], 2)
    last_bit = first_bit + 6

    if type_id == 4:
        keep_reading = True
        number = ""
        while keep_reading:
            keep_reading = bool(int(transmission[last_bit : last_bit + 1]))
            number += transmission[last_bit + 1 : last_bit + 5]
            last_bit += 5
    else:
        length_type_id = int(transmission[last_bit : last_bit + 1])
        last_bit += 1
        if length_type_id == 0:
            total_length = int(transmission[last_bit : last_bit + 15], 2)
            last_bit += 15
            subpackets = transmission[last_bit : last_bit + total_length]
            last_bit += total_length
        else:
            number_of_subpackets = transmission[last_bit : last_bit + 11]
            last_bit += 11
    last_bit += 4 - (last_bit - first_bit) % 4
    return 0


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_16/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
