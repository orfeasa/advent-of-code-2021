from collections import defaultdict


def part_one(filename: str) -> int:
    paper, x_max, y_max, folds = parse_input(filename)

    for direction, val in folds:
        paper, x_max, y_max = fold_paper(direction, val, paper, x_max, y_max)
        break  # just one fold

    return sum([int(val) for val in paper.values()])


def part_two(filename: str) -> int:
    paper, x_max, y_max, folds = parse_input(filename)

    for direction, val in folds:
        paper, x_max, y_max = fold_paper(direction, val, paper, x_max, y_max)

    print_paper(paper, x_max, y_max)


def fold_paper(direction, val, paper, x_max, y_max):
    if direction == "x":
        # folding along x0 means that the new grid becomes
        # (x, y) = ((x, y) or (2*x0-x, y)) for x in [0, x0-1] and y in [0, y_max]
        new_paper = defaultdict(bool)
        new_paper.update(
            {
                (x, y): paper[(x, y)] or paper[(2 * val - x, y)]
                for y in range(y_max + 1)
                for x in range(val)
            }
        )
        x_max = val - 1
    elif direction == "y":
        # folding along y0 means that the new grid becomes
        # (x, y) = ((x, y) or (x, 2*y0-y)) for x in [0, x_max] and y in [0, y0-1]
        new_paper = defaultdict(bool)
        new_paper.update(
            {
                (x, y): paper[(x, y)] or paper[(x, 2 * val - y)]
                for y in range(val)
                for x in range(x_max + 1)
            }
        )
        y_max = val - 1
    paper = new_paper
    return paper, x_max, y_max


def parse_input(filename: str):
    with open(filename) as f:
        dots, folds = f.read().split("\n\n")

    dots = list(
        map(lambda line: tuple(map(int, line.strip().split(","))), dots.split("\n"))
    )
    folds = list(
        map(
            lambda line: (
                line.lstrip("fold along ").split("=")[0],
                int(line.lstrip("fold along ").split("=")[1]),
            ),
            folds.strip().split("\n"),
        )
    )
    paper = defaultdict(bool)
    paper.update({(x, y): True for x, y, in dots})

    x_max = max(map(lambda coord: coord[0], dots))
    y_max = max(map(lambda coord: coord[1], dots))
    return paper, x_max, y_max, folds


def print_paper(paper: dict[tuple[int, int], bool], x_max, y_max: int):
    for y in range(y_max + 1):
        line_str = ""
        for x in range(x_max + 1):
            if paper[(x, y)]:
                line_str += "#"
            else:
                line_str += ".z"
        print(line_str)
    print("")


if __name__ == "__main__":
    input_path = "./day_13/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    part_two(input_path)
