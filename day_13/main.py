def part_one(filename: str) -> int:
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

    paper = {(x, y): True for x, y, in dots}

    x_max = max(map(lambda coord: coord[0], dots))
    y_max = max(map(lambda coord: coord[1], dots))

    direction, val = folds[0]
    if direction == "x":
        # folding along x0 means that the new grid becomes
        # (x, y) = ((x, y) or (2*x0-x, y)) for x in [0, x0-1] and y in [0, y_max]
        new_paper = {
            (x, y): paper[(x, y)] or paper[(2 * val - x, x)]
            for y in range(y_max)
            for x in range(val)
        }
        x_max = val - 1
        paper = new_paper

    # folding along y0 means that the new grid becomes
    # (x, y) = ((x, y) or (x, 2*y0-y)) for x in [0, x_max] and y in [0, y0-1]

    return 0


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_13/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
