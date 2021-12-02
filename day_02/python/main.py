def part_one(filename: str) -> int:
    with open(filename) as f:
        course = f.readlines()

    hor = 0
    ver = 0
    for step in course:
        dir_amount = step.strip().split()
        direction, amount = dir_amount[0], int(dir_amount[1])
        if direction == "forward":
            hor += amount
        elif direction == "down":
            ver += amount
        elif direction == "up":
            ver -= amount
        else:
            raise ValueError(f"{direction=}")
    return hor * ver


def part_two(filename: str) -> int:
    with open(filename) as f:
        course = f.readlines()

    hor = 0
    ver = 0
    aim = 0
    for step in course:
        dir_amount = step.strip().split()
        direction, amount = dir_amount[0], int(dir_amount[1])
        if direction == "forward":
            hor += amount
            ver += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
        else:
            raise ValueError(f"{direction=}")
    return hor * ver


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
