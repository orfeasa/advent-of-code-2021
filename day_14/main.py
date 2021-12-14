from collections import Counter


def part_one(filename: str) -> int:
    with open(filename) as f:
        template, rules = f.read().split("\n\n")
    rules = list(
        map(lambda rule: rule.strip().split(" -> "), rules.strip().split("\n"))
    )
    rules = {rule[0]: rule[1] for rule in rules}

    for _ in range(10):
        new_template = ""
        for i in range(len(template) - 1):
            pair = template[i : i + 2]
            new_template += pair[0]
            if pair in rules:
                new_template += rules[pair]
        new_template += pair[1]
        template = new_template

    counters = Counter(template)
    return max(counters.values()) - min(counters.values())


def part_two(filename: str) -> int:
    return 0


if __name__ == "__main__":
    input_path = "./day_14/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
