import re


def part_one(filename: str) -> int:
    regex = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
    with open(filename) as f:
        _, _, y_min, y_max = map(int, re.findall(regex, f.read().strip())[0])

    y = 0
    starting_y = {}
    for v_y0 in range(abs(y_min) + 1):
        y, v_y = 0, v_y0
        trajectory_y = []
        while y >= y_min:
            y += v_y
            trajectory_y.append(y)
            v_y -= 1
            if y_min <= y <= y_max:
                starting_y[v_y0] = max(trajectory_y)
                break

    return max(starting_y.values())


def part_two(filename: str) -> int:
    regex = r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)"
    with open(filename) as f:
        x_min, x_max, y_min, y_max = map(int, re.findall(regex, f.read().strip())[0])

    x, y = 0, 0
    initial_v = []
    for v_x0 in range(x_max + 1):
        for v_y0 in range(y_min, abs(y_min) + 1):
            v_x, v_y = v_x0, v_y0
            x, y = 0, 0
            while y >= y_min and x <= x_max:
                y += v_y
                x += v_x
                v_y -= 1
                v_x = v_x - 1 if v_x >= 1 else 0
                if y_min <= y <= y_max and x_min <= x <= x_max:
                    initial_v.append((v_x0, v_y0))
                    break

    return len(initial_v)


if __name__ == "__main__":
    input_path = "./day_17/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
