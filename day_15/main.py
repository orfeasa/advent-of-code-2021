from collections import defaultdict
import heapq


def part_one(filename: str) -> int:
    with open(filename) as f:
        nums = list(map(lambda n: [int(x) for x in list(n.strip())], f.readlines()))

    edges = [
        (f"{x},{y}", f"{x+dx},{y+dy}", nums[y + dy][x + dx])
        for y, line in enumerate(nums)
        for x, _ in enumerate(line)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= x + dx < len(nums[0]) and 0 <= y + dy < len(nums)
    ]

    cost, _ = dijkstra(edges, "0,0", f"{len(nums[0])-1},{len(nums)-1}")
    return cost


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
        for line in nums:
            new_line = []
            for val in line:
                new_line.append((val + inc) % 9 + 1)
            new_nums.append(new_line)
        new_rows.extend(new_nums)
    nums.extend(new_rows)

    edges = [
        (f"{x},{y}", f"{x+dx},{y+dy}", nums[y + dy][x + dx])
        for y, line in enumerate(nums)
        for x, _ in enumerate(line)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= x + dx < len(nums[0]) and 0 <= y + dy < len(nums)
    ]

    cost, _ = dijkstra(edges, "0,0", f"{len(nums[0])-1},{len(nums)-1}")
    return cost


def dijkstra(edges, initial, end):
    graph = defaultdict(list)
    for current, next, cost in edges:
        graph[current].append((cost, next))

    queue = [(0, initial, ())]
    seen = set()
    mins = {initial: 0}
    while queue:
        (cost1, v1, path) = heapq.heappop(queue)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == end:
                return (cost1, path)

            for cost2, v2 in graph.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost1 + cost2
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(queue, (next, v2, path))

    return float("inf"), None


if __name__ == "__main__":
    input_path = "./day_15/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
