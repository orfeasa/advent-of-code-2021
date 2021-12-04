def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: [int(i) for i in line.strip()], f.readlines()))

    counters = [sum(col) for col in zip(*nums)]
    gamma = int("".join([str(int(c > len(nums) / 2)) for c in counters]), 2)
    epsilon = int("".join([str(int(c < len(nums) / 2)) for c in counters]), 2)

    return gamma * epsilon


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: [int(i) for i in line.strip()], f.readlines()))

    counters = [sum(col) for col in zip(*nums)]
    gamma = "".join([str(int(c > len(nums) / 2)) for c in counters])
    epsilon = "".join([str(int(c < len(nums) / 2)) for c in counters])

    with open(filename) as f:
        nums = list(map(lambda line: line.strip(), f.readlines()))

    for suffix in range(1, len(nums[0])):
        prefix = gamma[:-suffix] + "1"
        matches = [x for x in nums if x.startswith(prefix)]
        if len(matches):
            oxygen = int(matches[0], 2)
            if len(matches) > 1:
                raise ValueError
            break
        prefix = gamma[:-suffix] + "0"
        matches = [x for x in nums if x.startswith(prefix)]
        if len(matches) > 0:
            oxygen = int(matches[0], 2)
            if len(matches) > 1:
                raise ValueError
            break

    for suffix in range(1, len(nums[0])):
        prefix = epsilon[:-suffix] + "1"
        matches = [x for x in nums if x.startswith(prefix)]
        if len(matches):
            co2 = int(matches[0], 2)
            if len(matches) > 1:
                raise ValueError
            break
        prefix = epsilon[:-suffix] + "0"
        matches = [x for x in nums if x.startswith(prefix)]
        if len(matches) > 0:
            co2 = int(matches[0], 2)
            if len(matches) > 1:
                raise ValueError
            break

    return oxygen * co2


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
