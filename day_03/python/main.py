def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: [int(i) for i in line.strip()], f.readlines()))

    counters = [sum(col) for col in zip(*nums)]
    gamma = [str(int(c > len(nums) / 2)) for c in counters]
    epsilon = [str(int(c < len(nums) / 2)) for c in counters]

    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
