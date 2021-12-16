from collections import defaultdict
from pprint import pprint


def part_one(filename: str) -> int:
    graph = parse_input(filename)
    return len(find_all_paths_once(graph, "start", "end"))


def part_two(filename: str) -> int:
    graph = parse_input(filename)
    return len(find_all_paths_twice(graph, "start", "end"))


def parse_input(filename: str) -> dict[str, list[str]]:
    graph = defaultdict(list)
    with open(filename) as f:
        connections = list(map(lambda s: s.strip().split("-"), f.readlines()))

    for (start, end) in connections:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def find_all_paths_twice(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        lowers = [x for x in path if x.islower()]
        visited_small_cave_twice = len(lowers) == len(set(lowers))
        if (
            node not in path
            or node.isupper()
            or (visited_small_cave_twice and node != "start")
        ):
            newpaths = find_all_paths_twice(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_all_paths_once(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = find_all_paths_once(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == "__main__":
    input_path = "./day_12/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
