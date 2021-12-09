from functools import reduce


def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    low_points = [
        val
        for y, line in enumerate(nums)
        for x, val in enumerate(line)
        if is_low_point(x, y, nums)
    ]

    return sum(low_points) + len(low_points)


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    basins = [
        bfs(x, y, nums)
        for y, line in enumerate(nums)
        for x, val in enumerate(line)
        if val != 9
    ]

    return reduce(lambda x, y: x * y, (sorted(basins, reverse=True)[:3]))


def bfs(x, y: int, nums: list[list[int]]) -> int:
    if (
        not nums
        or not 0 <= x < len(nums[0])
        or not 0 <= y < len(nums)
        or nums[y][x] == 9
    ):
        return 0

    nums[y][x] = 9
    count = 1
    count += bfs(x + 1, y, nums)
    count += bfs(x - 1, y, nums)
    count += bfs(x, y + 1, nums)
    count += bfs(x, y - 1, nums)
    return count


def is_low_point(x, y: int, nums: list[list[int]]) -> bool:
    adjacents = [
        nums[y + y1][x + x1]
        for x1, y1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= x + x1 < len(nums[0]) and 0 <= y + y1 < len(nums)
    ]
    return nums[y][x] < min(adjacents)


if __name__ == "__main__":
    input_path = "./day_09/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
