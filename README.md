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

| Day                                       | Name                    | Stars |
| ----------------------------------------- | ----------------------- | ----- |
| [01](https://adventofcode.com/2021/day/1) | Sonar Sweep             | ⭐⭐    |
| [02](https://adventofcode.com/2021/day/2) | Dive!                   | ⭐⭐    |
| [03](https://adventofcode.com/2021/day/3) | Binary Diagnostic       | ⭐⭐    |
| [04](https://adventofcode.com/2021/day/4) | Giant Squid             | ⭐⭐    |
| [05](https://adventofcode.com/2021/day/5) | Hydrothermal Venture    | ⭐⭐    |
| [06](https://adventofcode.com/2021/day/6) | Lanternfish             | ⭐⭐    |
| [07](https://adventofcode.com/2021/day/7) | The Treachery of Whales | ⭐⭐    |
| [08](https://adventofcode.com/2021/day/8) | Seven Segment Search    | ⭐⭐    |
| [09](https://adventofcode.com/2021/day/9) | Smoke Basin             | ⭐⭐    |

## Linting

```sh
black . && isort . && flake8 --max-line-length=100
```
