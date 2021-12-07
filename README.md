[![Go Report Card](https://goreportcard.com/badge/github.com/orfeasa/advent-of-code-2021)](https://goreportcard.com/report/github.com/orfeasa/advent-of-code-2021)

# 🎄 Advent of Code 2021 🎄

![AoC2021 logo](https://raw.githubusercontent.com/orfeasa/advent-of-code-2021/master/header.png)

## Summary

[Advent of Code](http://adventofcode.com/) is an annual Advent calendar of programming puzzles.

This year I am doing it in Go and Python.

## Running the code

To run the code of a specific day from the root directory run the following, replacing `xx` with the day number, `01` - `25`:

```sh
go run day_xx/go/main.go
python3 day_xx/python/main.py
```

Make sure you [have Go installed](https://golang.org/doc/install).

To run the code of all days run the script:

```sh
./run_all.sh
```

Make sure you have given permission to execute (`chmod +x run_all.sh`).

## Overview

| Day                                       | Name                    | Python | Go   |
| ----------------------------------------- | ----------------------- | ------ | ---- |
| [01](https://adventofcode.com/2021/day/1) | Sonar Sweep             | ⭐⭐   | ⭐⭐ |
| [02](https://adventofcode.com/2021/day/2) | Dive!                   | ⭐⭐   | ⭐⭐ |
| [03](https://adventofcode.com/2021/day/3) | Binary Diagnostic       | ⭐⭐   |      |
| [04](https://adventofcode.com/2021/day/4) | Giant Squid             | ⭐⭐   |      |
| [05](https://adventofcode.com/2021/day/5) | Hydrothermal Venture    | ⭐⭐   |      |
| [06](https://adventofcode.com/2021/day/6) | Lanternfish             | ⭐⭐   |      |
| [07](https://adventofcode.com/2021/day/7) | The Treachery of Whales | ⭐⭐   |      |

## Linting

```sh
gofmt -s -w . && git ls-files | grep .go | xargs golint
black . && isort . && flake8
```
