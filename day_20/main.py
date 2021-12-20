def part_one(filename: str) -> int:
    with open(filename) as f:
        algo_str, image_str = f.read().split("\n\n")
    image_str = image_str.strip().split("\n")
    algorithm = [1 if ch == "#" else 0 for ch in algo_str]
    image = []
    for line in image_str:
        image.append([1 if ch == "#" else 0 for ch in line])
    image, rest = enhance(image, algorithm)
    image, _ = enhance(image, algorithm, rest)
    return sum([sum(line) for line in image])


def part_two(filename: str) -> int:
    with open(filename) as f:
        algo_str, image_str = f.read().split("\n\n")
    image_str = image_str.strip().split("\n")
    algorithm = [1 if ch == "#" else 0 for ch in algo_str]
    image = []
    for line in image_str:
        image.append([1 if ch == "#" else 0 for ch in line])
    rest = 0
    for _ in range(50):
        image, rest = enhance(image, algorithm, rest)

    return sum([sum(line) for line in image])


def enhance(
    image: list[list[int]], algorithm: list[int], rest: int = 0
) -> list[list[int]]:
    new_image = []
    for y in range(-1, len(image) + 1):
        new_line = []
        for x in range(-1, len(image[0]) + 1):
            index = int(
                "".join(
                    [
                        str(image[y + dy][x + dx])
                        if 0 <= x + dx < len(image[0]) and 0 <= y + dy < len(image)
                        else str(rest)
                        for dy in [-1, 0, 1]
                        for dx in [-1, 0, 1]
                    ]
                ),
                2,
            )
            new_line.append(algorithm[index])
        TRIM_OFFEST = 0
        new_image.append(new_line)
    if algorithm[0]:
        rest = int(not rest)
    return new_image, rest


def print_image(image):
    for y, line in enumerate(image):
        new_line = ""
        for x, val in enumerate(line):
            new_line += "#" if val else "."
        print(new_line)
    print()


if __name__ == "__main__":
    input_path = "./day_20/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
