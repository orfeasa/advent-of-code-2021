from statistics import median


def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.read().strip().split(",")))

    return int(sum([abs(median(nums) - num) for num in nums]))


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.read().strip().split(",")))

    return min(
        [
            sum([fuel(x, point) for x in nums])
            for point in range(min(nums), max(nums) + 1)
        ]
    )


def fuel(start, end: int) -> int:
    d = max(start, end) - min(start, end)
    return int(d * (d + 1) / 2)


if __name__ == "__main__":
    input_path = "./day_07/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
