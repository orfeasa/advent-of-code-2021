def part_one(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver = 0, 0
    for step in course:
        direction, value = step[0], int(step[1])
        if direction == "forward":
            hor += value
        elif direction == "down":
            ver += value
        elif direction == "up":
            ver -= value
    return hor * ver


def part_two(filename: str) -> int:
    with open(filename) as f:
        course = map(lambda line: line.strip().split(), f.readlines())

    hor, ver, aim = 0, 0, 0
    for step in course:
        direction, value = step[0], int(step[1])
        if direction == "forward":
            hor += value
            ver += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value
    return hor * ver


if __name__ == "__main__":
    input_path = "./day_02/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
