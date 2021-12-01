def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    return count_sliding_window_inceases(nums, 1)


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    return count_sliding_window_inceases(nums, 3)


def count_sliding_window_inceases(nums: list[int], size: int) -> int:
    count = 0
    for i in range(len(nums) - size):
        if sum(nums[i + 1 : i + 1 + size]) > sum(nums[i : i + size]):
            count += 1
    return count


if __name__ == "__main__":
    input_path = "./day_01/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
