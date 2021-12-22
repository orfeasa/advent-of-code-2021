import re
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Cuboid:
    is_on: bool
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    def get_volume(self):
        return (
            (self.x_max - self.x_min)
            * (self.y_max - self.y_min)
            * (self.z_max - self.z_min)
        )


def part_one(filename: str) -> int:
    cuboids = parse_input(filename)

    space = defaultdict(bool)
    for cuboid in cuboids:
        x_start = cuboid.x_min if cuboid.x_min > -50 else -50
        x_stop = cuboid.x_max if cuboid.x_max < 50 else 50
        for x in range(x_start, x_stop + 1):
            y_start = cuboid.y_min if cuboid.y_min > -50 else -50
            y_stop = cuboid.y_max if cuboid.y_max < 50 else 50
            for y in range(y_start, y_stop + 1):
                z_start = cuboid.z_min if cuboid.z_min > -50 else -50
                z_stop = cuboid.z_max if cuboid.z_max < 50 else 50
                for z in range(z_start, z_stop + 1):
                    space[(x, y, z)] = cuboid.is_on

    return list(space.values()).count(True)


def part_two(filename: str) -> int:
    return 0


def parse_input(filename: str) -> list["Cuboid"]:
    regex = r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
    cuboids = []
    with open(filename) as f:
        for line in f.readlines():
            is_on, x_min, x_max, y_min, y_max, z_min, z_max = re.findall(
                regex, line.strip()
            )[0]
            cuboids.append(
                Cuboid(
                    is_on == "on",
                    *list(map(int, [x_min, x_max, y_min, y_max, z_min, z_max])),
                )
            )
    return cuboids


if __name__ == "__main__":
    input_path = "./day_22/test_input3.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))
