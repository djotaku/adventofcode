// AoC 2017 Day 01 - Inverse Captcha

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// OneLine returns the input file if it's just one line of text
func OneLine(fileName string) (string, error) {
	var inputLine string
	file, err := os.Open(fileName)
	if err != nil {
		return inputLine, err
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inputLine = scanner.Text()
	}
	err = file.Close()
	if err != nil {
		return inputLine, err
	}
	return inputLine, nil
}

// detectDoubles takes in a string of numbers. It returns the sum of all doubles
// Also if the first and last number are the same, those are considered doubles, too.
func detectDoubles(numbers string) (int, int) {
	doubleSum := 0
	lookAhead := len(numbers) / 2
	part2Sum := 0
	for index, number := range numbers {
		if index+1 < len(numbers) {
			if string(number) == string(numbers[index+1]) {

				intyNumber, _ := strconv.Atoi(string(numbers[index]))
				doubleSum += intyNumber
			}
		}
		checkIndex := (index + lookAhead) % len(numbers)
		if string(number) == string(numbers[checkIndex]) {
			intyNumber, _ := strconv.Atoi(string(number))
			part2Sum += intyNumber
		}
	}
	if numbers[0] == numbers[len(numbers)-1] {
		intyNumber, _ := strconv.Atoi(string(numbers[numbers[0]]))
		doubleSum += intyNumber
	}
	return doubleSum, part2Sum
}

func main() {
	captcha, err := OneLine("../input.txt")
	if err != nil {
		print(err)
	}
	//captcha := "1122"
	partOne, partTwo := detectDoubles(captcha)
	fmt.Printf("The solution to the captcha for part 1 is %d\n", partOne)
	fmt.Printf("The solution to the captcha for part 2 is %d\n", partTwo)
}
