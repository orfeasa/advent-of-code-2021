from collections import Counter, defaultdict

def part_one(filename: str) -> int:
    template, rules = parse_input(filename)

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

class Element():
    def __init__(self, value:str, next=None) -> None:
        self.value=value
        self.next=next


def part_two(filename: str) -> int:
    template, rules = parse_input(filename)

    start = Element(template[0])
    prev = start
    for ch in template[1:]:
        current = Element(ch)
        prev.next = current
        prev = current

    for _ in range(40):
        print(f"Step {_+1}")
        current = start
        while current.next:
            pair = current.value + current.next.value
            if pair in rules:
                new = Element(rules[pair])
                new.next = current.next
                current.next = new
                current = new.next

    counters = defaultdict(int)
    current = start
    while current:
        counters[current.value] += 1
        current = current.next

    return max(counters.values()) - min(counters.values())

def print_sequence(start: Element) -> None:
    current =start
    sequence = ""
    while current:
        sequence += current.value
        current = current.next
    print(sequence)

def parse_input(filename:str) -> tuple[str, dict[str,str]]:
    with open(filename) as f:
        template, rules = f.read().split("\n\n")
    rules = list(
        map(lambda rule: rule.strip().split(" -> "), rules.strip().split("\n"))
    )
    rules = {rule[0]: rule[1] for rule in rules}
    return template, rules

if __name__ == "__main__":
    input_path = "./day_14/test_input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
