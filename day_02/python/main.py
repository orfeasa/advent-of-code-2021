def part_one(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver = 0, 0
    for step in course:
        direction, amount = step[0], int(step[1])
        if direction == "forward":
            hor += amount
        elif direction == "down":
            ver += amount
        elif direction == "up":
            ver -= amount
    return hor * ver


def part_two(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver, aim = 0, 0, 0
    for step in course:
        direction, amount = step[0], int(step[1])
        if direction == "forward":
            hor += amount
            ver += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return hor * ver


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
