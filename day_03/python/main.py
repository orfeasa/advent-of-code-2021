def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: [int(i) for i in line.strip()], f.readlines()))

    counters = [sum(col) for col in zip(*nums)]
    gamma = int("".join([str(int(c > len(nums) / 2)) for c in counters]), 2)
    epsilon = int("".join([str(int(c < len(nums) / 2)) for c in counters]), 2)

    return gamma * epsilon


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
