def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    count_flashes = 0
    for _ in range(100):
        nums = next_step(nums)
        count_flashes += sum([int(num == 0) for line in nums for num in line])

    return count_flashes


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    synced = False
    step = 0
    while not synced:
        step += 1
        nums = next_step(nums)
        synced = all([num == nums[0][0] for line in nums for num in line])
    return step


def next_step(nums):
    for y, line in enumerate(nums):
        for x, _ in enumerate(line):
            nums[y][x] += 1

    to_flash = {
        (x, y) for y, line in enumerate(nums) for x, val in enumerate(line) if val > 9
    }

    flashed = set()

    while to_flash:
        x0, y0 = to_flash.pop()
        flashed.add((x0, y0))
        for x, y in get_adjacents(x0, y0, nums):
            if (x, y) not in flashed | to_flash:
                nums[y][x] += 1
                if nums[y][x] > 9:
                    to_flash.add((x, y))

    for y, line in enumerate(nums):
        for x, _ in enumerate(line):
            if nums[y][x] > 9:
                nums[y][x] = 0
    return nums


def get_adjacents(x, y: int, nums: list[list[int]]) -> list[tuple[int, int]]:
    return [
        (x + dx, y + dy)
        for dx, dy in [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        if 0 <= x + dx < len(nums[0]) and 0 <= y + dy < len(nums)
    ]


if __name__ == "__main__":
    input_path = "./day_11/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
