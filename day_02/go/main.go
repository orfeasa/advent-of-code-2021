package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputPath := "./day_02/input.txt"
	fmt.Println("--- Part One ---")
	fmt.Println(part1(inputPath))

	fmt.Println("--- Part Two ---")
	fmt.Println(part2(inputPath))
}

func part1(inputPath string) int {
	course := readStrings(inputPath)
	hor := 0
	ver := 0
	for _, step := range course {
		dirValue := strings.Split(step, " ")
		direction := dirValue[0]
		value := toInt(dirValue[1])
		switch direction {
		case "forward":
			hor += value
		case "down":
			ver += value
		case "up":
			ver -= value
		}
	}
	return hor * ver
}

func part2(inputPath string) int {
	course := readStrings(inputPath)
	hor := 0
	ver := 0
	aim := 0
	for _, step := range course {
		dirValue := strings.Split(step, " ")
		direction := dirValue[0]
		value := toInt(dirValue[1])
		switch direction {
		case "forward":
			hor += value
			ver += aim * value
		case "down":
			aim += value
		case "up":
			aim -= value
		}
	}
	return hor * ver
}

func readStrings(filename string) []string {
	file, err := os.Open(filename)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var text []string
	for scanner.Scan() {
		text = append(text, strings.TrimRight(scanner.Text(), "\n"))
	}
	return text
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

func max(numbers []int) int {
	currMax := numbers[0]
	for _, val := range numbers {
		if val > currMax {
			currMax = val
		}
	}
	return currMax
}

func min(numbers []int) int {
	currMin := numbers[0]
	for _, val := range numbers {
		if val < currMin {
			currMin = val
		}
	}
	return currMin
}
