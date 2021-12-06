from collections import Counter, defaultdict

def part_one(filename: str) -> int:
    return lanternfish_population(filename, 80)


def part_two(filename: str) -> int:
    return lanternfish_population(filename, 256)

def lanternfish_population(filename: str, days: int) -> int:
    with open(filename) as f:
        initial_state = list(map(int, f.read().split(",")))

    ages = Counter(initial_state)

    for _ in range(days):
        new_ages = defaultdict(int)
        for age in ages:
            if age == 0:
                new_ages[6] += ages[0]
                new_ages[8] += ages[0]
            else:
                new_ages[age-1] += ages[age]
        ages = new_ages

    return sum(ages.values())



if __name__ == "__main__":
    input_path = "./day_06/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
