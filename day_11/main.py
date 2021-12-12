def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    count_flashes = 0
    print("Before any steps:")
    print_nums(nums)
    for step in range(101 + 1):
        increment_queue = [
            (x, y) for y, line in enumerate(nums) for x, _ in enumerate(line)
        ]

        flashed = set()
        while increment_queue:
            x, y = increment_queue.pop(0)
            nums[y][x] += 1
            if nums[y][x] > 9 and (x, y) not in flashed:
                flashed.add((x, y))
                increment_queue.extend(get_adjacents(x, y, nums))

        for y, line in enumerate(nums):
            for x, _ in enumerate(line):
                if nums[y][x] > 9:
                    nums[y][x] = 0

        count_flashes += len(flashed)
        print(f"After step {step+1}")
        print_nums(nums)
        print(f"Flashed: {len(flashed)}: {flashed}")

    return count_flashes


def part_two(filename: str) -> int:
    return 0


def get_adjacents(x, y: int, nums: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (y + y1, x + x1)
        for x1, y1 in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        if 0 <= x + x1 < len(nums[0]) and 0 <= y + y1 < len(nums)
    ]


def print_nums(nums: list[list[int]]):
    for line in nums:
        line_str = ""
        for ch in line:
            line_str += str(ch)
        print(line_str)
    print("")


if __name__ == "__main__":
    input_path = "./day_11/test_input2.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
