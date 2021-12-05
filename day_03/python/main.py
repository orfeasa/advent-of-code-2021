def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: [int(i) for i in line.strip()], f.readlines()))

    counters = [sum(col) for col in zip(*nums)]
    gamma = int("".join([str(int(c > len(nums) / 2)) for c in counters]), 2)
    epsilon = int("".join([str(int(c < len(nums) / 2)) for c in counters]), 2)

    return gamma * epsilon


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda line: line.strip(), f.readlines()))

    prefix = ""
    nums_left = nums
    for pos in range(len(nums[0])):
        counters = [sum(map(int, col)) for col in zip(*nums_left)]
        if counters[pos] >= len(nums_left) / 2:
            prefix += "1"
        else:
            prefix += "0"
        nums_left = [x for x in nums_left if x.startswith(prefix)]
        if len(nums_left) == 1:
            oxygen = nums_left[0]
            break

    prefix = ""
    nums_left = nums
    for pos in range(len(nums[0])):
        counters = [sum(map(int, col)) for col in zip(*nums_left)]
        if counters[pos] < len(nums_left) / 2:
            prefix += "1"
        else:
            prefix += "0"
        nums_left = [x for x in nums_left if x.startswith(prefix)]
        if len(nums_left) == 1:
            co2 = nums_left[0]
            break

    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    input_path = "./day_03/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
