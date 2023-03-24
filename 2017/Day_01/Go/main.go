// AoC 2017 Day 01 - Inverse Captcha

package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
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
func detectDoubles(numbers string) int {
	re := regexp.MustCompile(`'(\d)(?=\1)'`)
	matches := re.FindStringSubmatch(numbers)
	doubleSum := 0
	for _, number := range matches {
		numberAsNumber, err := strconv.Atoi(number)
		if err != nil {
			print(err)
		}
		doubleSum += numberAsNumber
	}
	if numbers[0] == numbers[len(numbers)-1] {
		doubleSum += int(numbers[0])
	}
	return doubleSum
}

func main() {
	captcha, err := OneLine("../input.txt")
	if err != nil {
		print(err)
	}
	partOne := detectDoubles(captcha)
	fmt.Printf("The solution to the captcha for part 1 is %d\n", partOne)
}
