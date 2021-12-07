from collections import defaultdict


def part_one(filename: str) -> int:
    with open(filename) as f:
        lines = list(map(lambda line: line.strip().split(" -> "), f.readlines()))

    lines = [
        [list(map(int, line[0].split(","))), list(map(int, line[1].split(",")))]
        for line in lines
    ]

    pairs_to_lines = defaultdict(int)
    for pairs in lines:
        start = pairs[0]
        end = pairs[1]

        if start[0] == end[0] or start[1] == end[1]:
            x_min = min(start[0], end[0])
            x_max = max(start[0], end[0])
            for x in range(x_min, x_max + 1):
                y_min = min(start[1], end[1])
                y_max = max(start[1], end[1])
                for y in range(y_min, y_max + 1):
                    pairs_to_lines[(x, y)] += 1
    counter = 0
    for pairs, lines in pairs_to_lines.items():
        if lines >= 2:
            counter += 1

    return counter


def part_two(filename: str) -> int:
    with open(filename) as f:
        lines = list(map(lambda line: line.strip().split(" -> "), f.readlines()))

    lines = [
        [list(map(int, line[0].split(","))), list(map(int, line[1].split(",")))]
        for line in lines
    ]

    pairs_to_lines = defaultdict(int)
    for pairs in lines:
        start = pairs[0]
        end = pairs[1]
        x_min = min(start[0], end[0])
        x_max = max(start[0], end[0])
        y_min = min(start[1], end[1])
        y_max = max(start[1], end[1])
        if start[0] == end[0] or start[1] == end[1]:
            for x in range(x_min, x_max + 1):
                for y in range(y_min, y_max + 1):
                    pairs_to_lines[(x, y)] += 1
        else:
            for step in range(0, x_max - x_min + 1):
                pairs_to_lines[(x + step, y + step)] += 1
    counter = 0
    for pairs, lines in pairs_to_lines.items():
        if lines >= 2:
            counter += 1

    return counter


if __name__ == "__main__":
    input_path = "./day_05/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))