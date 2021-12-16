from collections import defaultdict


class Graph:
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight


def create_graph_from_nums(nums):
    graph = Graph()

    edges = [
        (f"{x},{y}", f"{x+dx},{y+dy}", nums[y + dy][x + dx])
        for y, line in enumerate(nums)
        for x, _ in enumerate(line)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= x + dx < len(nums[0]) and 0 <= y + dy < len(nums)
    ]

    for edge in edges:
        graph.add_edge(*edge)
    return graph


def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    graph = create_graph_from_nums(nums)

    path = dijsktra(graph, "0,0", f"{len(nums[0])-1},{len(nums)-1}")
    total_risk = 0
    for i in range(len(path) - 1):
        total_risk += graph.weights[(path[i], path[i + 1])]

    return total_risk


def part_two(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    # add horizontal
    for line in nums:
        new_line = []
        for inc in range(4):
            new_line += [(val + inc) % 9 + 1 for val in line]
        line.extend(new_line)

    # add vertical
    new_rows = []
    for inc in range(4):
        new_nums = []
        for y, line in enumerate(nums):
            new_line = []
            for x, val in enumerate(line):
                new_line.append((val + inc) % 9 + 1)
            new_nums.append(new_line)
        new_rows.extend(new_nums)
    nums.extend(new_rows)

    # for y, line in enumerate(nums):
    #     print("".join(map(str, line)))

    graph = create_graph_from_nums(nums)

    path = dijsktra(graph, "0,0", f"{len(nums[0])-1},{len(nums)-1}")
    total_risk = 0
    for i in range(len(path) - 1):
        total_risk += graph.weights[(path[i], path[i + 1])]
    return total_risk


def print_path(nums, path):
    for y in range(len(nums)):
        line = ""
        for x in range(len(nums[0])):
            if f"{x},{y}" in path:
                line += "#"
            else:
                line += "."
        print(line)


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {
            node: shortest_paths[node] for node in shortest_paths if node not in visited
        }
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


if __name__ == "__main__":
    input_path = "./day_15/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
