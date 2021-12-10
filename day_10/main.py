from statistics import median

corrupt_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
incomplete_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def part_one(filename: str) -> int:
    with open(filename) as f:
        lines = map(lambda line: line.strip(), f.readlines())

    total = 0
    for line in lines:
        queue = []
        for ch in line:
            if ch in matches:
                queue.append(matches[ch])
            else:
                if not queue or ch != queue.pop():
                    total += corrupt_scores[ch]
                    break

    return total


def part_two(filename: str) -> int:
    with open(filename) as f:
        lines = map(lambda line: line.strip(), f.readlines())

    scores = []
    for line in lines:
        queue = []
        is_corrupted = False
        for ch in line:
            if ch in matches:
                queue.append(matches[ch])
            else:
                if not queue or ch != queue.pop():
                    is_corrupted = True
                    break
        if not is_corrupted:
            score = 0
            while queue:
                ch = queue.pop()
                score = 5 * score + incomplete_scores[ch]
            scores.append(score)

    return median(scores)


if __name__ == "__main__":
    input_path = "./day_10/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
