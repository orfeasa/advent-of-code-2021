# 🎄 Advent of Code 2021 🎄

![AoC2021 logo](https://raw.githubusercontent.com/orfeasa/advent-of-code-2021/master/header.png)

## Summary

[Advent of Code](http://adventofcode.com/) is an annual Advent calendar of programming puzzles.
This year I am doing it in Python.

## Running the code

To run the code of a specific day from the root directory run the following, replacing `xx` with the day number, `01` - `25`:

```sh
python3 day_xx/main.py
```

To run the code of all days run the script:

```sh
./run_all.sh
```

Make sure you have given permission to execute (`chmod +x run_all.sh`).

## Overview

| Day                                        | Name                    | Stars |
| ------------------------------------------ | ----------------------- | ----- |
| [01](https://adventofcode.com/2021/day/1)  | Sonar Sweep             | ⭐⭐    |
| [02](https://adventofcode.com/2021/day/2)  | Dive!                   | ⭐⭐    |
| [03](https://adventofcode.com/2021/day/3)  | Binary Diagnostic       | ⭐⭐    |
| [04](https://adventofcode.com/2021/day/4)  | Giant Squid             | ⭐⭐    |
| [05](https://adventofcode.com/2021/day/5)  | Hydrothermal Venture    | ⭐⭐    |
| [06](https://adventofcode.com/2021/day/6)  | Lanternfish             | ⭐⭐    |
| [07](https://adventofcode.com/2021/day/7)  | The Treachery of Whales | ⭐⭐    |
| [08](https://adventofcode.com/2021/day/8)  | Seven Segment Search    | ⭐⭐    |
| [09](https://adventofcode.com/2021/day/9)  | Smoke Basin             | ⭐⭐    |
| [10](https://adventofcode.com/2021/day/10) | Syntax Scoring          | ⭐⭐    |
| [11](https://adventofcode.com/2021/day/11) | Dumbo Octopus           | ⭐⭐    |
| [12](https://adventofcode.com/2021/day/12) | Passage Pathing         |       |
| [13](https://adventofcode.com/2021/day/13) | Transparent Origami     | ⭐⭐    |
| [14](https://adventofcode.com/2021/day/14) | Extended Polymerization | ⭐⭐    |
| [15](https://adventofcode.com/2021/day/15) | Chiton                  | ⭐⭐    |
| [16](https://adventofcode.com/2021/day/16) | Packet Decoder          |       |
| [17](https://adventofcode.com/2021/day/17) | TBA                     |       |
| [18](https://adventofcode.com/2021/day/18) | TBA                     |       |
| [19](https://adventofcode.com/2021/day/19) | TBA                     |       |
| [20](https://adventofcode.com/2021/day/20) | TBA                     |       |
| [21](https://adventofcode.com/2021/day/21) | TBA                     |       |
| [22](https://adventofcode.com/2021/day/22) | TBA                     |       |
| [23](https://adventofcode.com/2021/day/23) | TBA                     |       |
| [24](https://adventofcode.com/2021/day/24) | TBA                     |       |
| [25](https://adventofcode.com/2021/day/25) | TBA                     |       |

## New Day

To generate the directory for the current day, save your browser cookie in a file called `cookie.txt` and run the new day script:

```sh
./new_day.sh
```

### How to get your cookie

A session cookie is a small piece of data used to authenticate yourself to the
Advent of Code web servers. It is not human-readable and might look something
like this `53616c7465645f5fbd2d445187c5dc5463efb7020021c273c3d604b5946f9e87e2dc30b649f9b2235e8cd57632e415cb`.

To learn more about authentication cookies check [this Wikipedia article](https://en.wikipedia.org/wiki/HTTP_cookie)

To get your cookie, go to the [Advent of Code website](https://adventofcode.com/), and while logged in.

- For Firefox: right and select "Inspect Element" and in the "Storage" tab select "Cookies" → "https://adventofcode.com"
- For Chrome: right and select "Inspect" and in the "Application" tab select "Cookies" → "https://adventofcode.com"

Then find the row with "session" as name, copy the value and paste it in your newly created `cookie.txt` file

## Linting

```sh
black . && isort . && flake8 --max-line-length=100
```
