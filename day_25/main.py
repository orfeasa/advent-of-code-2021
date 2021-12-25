def part_one(filename: str) -> int:
    with open(filename) as f:
        sea_map = list(map(lambda line: [x for x in line.strip()], f.readlines()))

    east_facing = set()
    south_facing = set()
    for y, line in enumerate(sea_map):
        for x, _ in enumerate(line):
            if sea_map[y][x] == ">":
                east_facing.add((x, y))
            if sea_map[y][x] == "v":
                south_facing.add((x, y))

    cucumbers_moved = True
    steps = 0
    while cucumbers_moved:
        steps += 1
        cucumbers_moved = False
        east_to_move = set()
        for x, y in east_facing:
            x1, y1 = (x + 1) % len(line), y
            if sea_map[y][x] == ">" and sea_map[y1][x1] == ".":
                east_to_move.add((x, y))
        if len(east_to_move):
            cucumbers_moved = True
        for x, y in east_to_move:
            x1, y1 = (x + 1) % len(line), y
            sea_map[y1][x1] = ">"
            sea_map[y][x] = "."
            east_facing.remove((x, y))
            east_facing.add((x1, y1))

        south_to_move = set()
        for x, y in south_facing:
            x1, y1 = x, (y + 1) % len(sea_map)
            if sea_map[y][x] == "v" and sea_map[y1][x1] == ".":
                south_to_move.add((x, y))
        if len(south_to_move):
            cucumbers_moved = True
        for x, y in south_to_move:
            x1, y1 = x, (y + 1) % len(sea_map)
            sea_map[y1][x1] = "v"
            sea_map[y][x] = "."
            south_facing.remove((x, y))
            south_facing.add((x1, y1))

    return steps


if __name__ == "__main__":
    input_path = "./day_25/input.txt"
    print("---Part One---")
    print(part_one(input_path))
