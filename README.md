[![Go Report Card](https://goreportcard.com/badge/github.com/orfeasa/advent-of-code-2021)](https://goreportcard.com/report/github.com/orfeasa/advent-of-code-2021)

# 🎄 Advent of Code 2021 🎄

![AoC2021 logo](https://raw.githubusercontent.com/orfeasa/advent-of-code-2021/master/header.png)

## Summary

[Advent of Code](http://adventofcode.com/) is an annual Advent calendar of programming puzzles.

This year I am doing it in Go.

## Running the code

To run the code of a specific day from the root directory run the following, replacing `XX` with the day number, `01` - `25`:

```sh
go run day_XX/main.go
```

Make sure you [have Go installed](https://golang.org/doc/install).

To run the code of all days run the script:

```sh
./run_all.sh
```

Make sure you have given permission to execute (`chmod +x run_all.sh`).

## Overview

| Day                                        | Name | Stars |
| ------------------------------------------ | ---- | ----- |
| [01](https://adventofcode.com/2021/day/1)  |      |   |
<!-- | [02](https://adventofcode.com/2021/day/2)  |      | ⭐⭐  |
| [03](https://adventofcode.com/2021/day/3)  |      | ⭐⭐  |
| [04](https://adventofcode.com/2021/day/4)  |      | ⭐⭐  |
| [05](https://adventofcode.com/2021/day/5)  |      | ⭐⭐  |
| [06](https://adventofcode.com/2021/day/6)  |      | ⭐⭐  |
| [07](https://adventofcode.com/2021/day/7)  |      | ⭐⭐  |
| [08](https://adventofcode.com/2021/day/8)  |      | ⭐⭐  |
| [09](https://adventofcode.com/2021/day/9)  |      | ⭐⭐  |
| [10](https://adventofcode.com/2021/day/10) |      | ⭐⭐  |
| [11](https://adventofcode.com/2021/day/11) |      | ⭐⭐  |
| [12](https://adventofcode.com/2021/day/12) |      | ⭐⭐  |
| [13](https://adventofcode.com/2021/day/13) |      | ⭐⭐  |
| [14](https://adventofcode.com/2021/day/14) |      | ⭐⭐  |
| [15](https://adventofcode.com/2021/day/15) |      | ⭐⭐  |
| [16](https://adventofcode.com/2021/day/16) |      | ⭐⭐  |
| [17](https://adventofcode.com/2021/day/17) |      | ⭐⭐  |
| [18](https://adventofcode.com/2021/day/18) |      | ⭐⭐  |
| [19](https://adventofcode.com/2021/day/19) |      | ⭐⭐  |
| [20](https://adventofcode.com/2021/day/20) |      | ⭐⭐  |
| [21](https://adventofcode.com/2021/day/21) |      | ⭐⭐  |
| [22](https://adventofcode.com/2021/day/22) |      | ⭐⭐  |
| [23](https://adventofcode.com/2021/day/23) |      | ⭐⭐  |
| [24](https://adventofcode.com/2021/day/24) |      | ⭐⭐  |
| [25](https://adventofcode.com/2021/day/25) |      | ⭐⭐  | -->

## Linting

```sh
gofmt -s -w .
git ls-files | grep .go | xargs golint
```
