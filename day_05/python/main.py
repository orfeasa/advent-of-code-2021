def part_one(filename: str) -> int:
    with open(filename) as f:
        lines = list(map(lambda line: line.strip().split(" -> "), f.readlines()))

    lines = [[l[0].split(","), l[1].split(",")] for l in lines]
    return 0


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_05/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
