package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	inputPath := "./day_01/input.txt"
	fmt.Println("--- Part One ---")
	fmt.Println(part1(inputPath))

	fmt.Println("--- Part Two ---")
	fmt.Println(part2(inputPath))
}

func part1(inputPath string) int {
	nums := readNumbers(inputPath)
	return countSlidingWindowIncrease(nums, 1)
}

func part2(inputPath string) int {
	nums := readNumbers(inputPath)
	return countSlidingWindowIncrease(nums, 3)
}

func countSlidingWindowIncrease(numbers []int, size int) int {
	count := 0
	for i := 0; i < len(numbers)-size; i++ {
		if sum(numbers[i+1:i+size+1]) > sum(numbers[i:i+size]) {
			count++
		}
	}
	return count
}

func readNumbers(filename string) []int {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	Scanner := bufio.NewScanner(file)

	var numbers []int
	for Scanner.Scan() {
		numbers = append(numbers, toInt(Scanner.Text()))
	}
	return numbers
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func toInt(s string) int {
	result, err := strconv.Atoi(s)
	check(err)
	return result
}

func sum(numbers []int) int {
	sum := 0
	for _, num := range numbers {
		sum += num
	}
	return sum
}
