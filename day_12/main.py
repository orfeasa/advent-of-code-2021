from collections import defaultdict
from collections.abc import Callable


def part_one(filename: str) -> int:
    graph = parse_input(filename)
    return len(find_all_paths(graph, "start", "end", once))


def part_two(filename: str) -> int:
    graph = parse_input(filename)
    return len(find_all_paths(graph, "start", "end", twice))


def parse_input(filename: str) -> dict[str, list[str]]:
    graph = defaultdict(list)
    with open(filename) as f:
        connections = list(map(lambda s: s.strip().split("-"), f.readlines()))

    for (start, end) in connections:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def find_all_paths(
    graph: dict[str, list[str]],
    start,
    end: str,
    small_caves_strategy: Callable,
    path=[],
):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or small_caves_strategy(path, node):
            newpaths = find_all_paths(graph, node, end, small_caves_strategy, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def once(path: list[str], node: str) -> bool:
    return node.isupper()


def twice(path: list[str], node: str) -> bool:
    lowers = [x for x in path if x.islower()]
    visited_small_cave_twice = len(lowers) == len(set(lowers))
    return node.isupper() or (visited_small_cave_twice and node != "start")


if __name__ == "__main__":
    input_path = "./day_12/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
