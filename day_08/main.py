from collections import Counter
from functools import reduce

number_to_segments = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

segments_to_numbers = {"".join(sorted(v)): k for k, v in number_to_segments.items()}


def part_one(filename: str) -> int:
    with open(filename) as f:
        lines = list(map(lambda s: s.strip().split(" | "), f.readlines()))
        lines = list(map(lambda l: (l[0].split(), l[1].split()), lines))

    unique_lengths = [len(number_to_segments[d]) for d in [1, 4, 7, 8]]
    counter = 0
    for _, output_values in lines:
        for value in output_values:
            if len(value) in unique_lengths:
                counter += 1
    return counter


def part_two(filename: str) -> int:
    with open(filename) as f:
        lines = list(map(lambda s: s.strip().split(" | "), f.readlines()))
        lines = list(map(lambda l: (l[0].split(), l[1].split()), lines))

    total = 0
    for signal_patterns, output_values in lines:
        decoded = decode_patterns(signal_patterns)
        decoded_values = []
        for output_value in output_values:
            decoded_value = ""
            for c in output_value:
                decoded_value += decoded[c]
            decoded_values.append("".join(sorted(decoded_value)))

        total += int(
            "".join(map(str, [segments_to_numbers[x] for x in decoded_values]))
        )

    return total


def decode_patterns(signal_patterns: list[str]) -> dict[str, str]:
    decoded = {}

    # 7 ("acf") - 1 ("cf") = "a"
    seven = next(x for x in signal_patterns if len(x) == len(number_to_segments[7]))
    one = next(x for x in signal_patterns if len(x) == len(number_to_segments[1]))
    a_char = next(a for a in seven if a not in one)
    decoded[a_char] = "a"

    # Counter({'f': 9, 'c': 8, 'a': 8, 'd': 7, 'g': 7, 'b': 6, 'e': 4})
    char_count = Counter(reduce(lambda x, y: x + y, signal_patterns))
    for char, count in char_count.items():
        if count == 4:
            decoded[char] = "e"
        elif count == 6:
            decoded[char] = "b"
        elif count == 9:
            decoded[char] = "f"
        elif count == 8 and char != a_char:
            decoded[char] = "c"
        elif count == 7:
            # distinguish between d and g as d is present in 4 ("bcdf")
            four = next(
                x for x in signal_patterns if len(x) == len(number_to_segments[4])
            )
            if char in four:
                decoded[char] = "d"
            else:
                decoded[char] = "g"

    return decoded


if __name__ == "__main__":
    input_path = "./day_08/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
