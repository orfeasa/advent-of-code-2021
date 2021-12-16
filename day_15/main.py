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
        for y, line in enumerate(nums):
            new_line = []
            for x, val in enumerate(line):
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


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}
    while q:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(q, (next, v2, path))

    return float("inf"), None


if __name__ == "__main__":
    input_path = "./day_15/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
