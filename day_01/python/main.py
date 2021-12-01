def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    count = 0
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            count += 1
    return count


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(int, f.readlines()))
    count = 0
    for i in range(len(nums) - 3):
        if sum(nums[i + 1 : i + 1 + 3]) > sum(nums[i : i + 3]):
            count += 1
    return count


if __name__ == "__main__":
    input_path = "./day_01/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
