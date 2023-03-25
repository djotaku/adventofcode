// Advent of Code 2018 Day 01 - Chronal Calibration
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// MultipleLinesNumbers returns the input file if it contains multiple lines of text which are numbers
func MultipleLinesNumbers(fileName string) ([]int, error) {
	inputSlice := make([]int, 0)
	file, err := os.Open(fileName)
	if err != nil {
		return inputSlice, err
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		thisNumber, _ := strconv.Atoi(scanner.Text())
		inputSlice = append(inputSlice, thisNumber)
	}
	err = file.Close()
	if err != nil {
		return inputSlice, err
	}
	return inputSlice, nil
}

// totalFrequencies sums up the frequencies in the slice and returns the total
func totalFrequencies(frequencySlice []int) int {
	total := 0
	for _, number := range frequencySlice {
		total += number
	}
	return total
}

// findRepeatedFrequency works like totalFrequencies except it stops when it gets to one it's seen before
func findRepeatedFrequency(frequencySlice []int) int {
	fakeSet := map[int]bool{} // this will function as a set since Go doesn't have them built in
	total := 0
	for {
		for _, number := range frequencySlice {
			total += number
			if fakeSet[total] {
				return total
			} else {
				fakeSet[total] = true
			}
		}
	}
	return 0
}

func main() {
	frequencyChanges, err := MultipleLinesNumbers("../input.txt")
	if err != nil {
		print(err)
	}
	partOne := totalFrequencies(frequencyChanges)
	fmt.Printf("The sum of the frequencies is %v\n", partOne)
	partTwo := findRepeatedFrequency(frequencyChanges)
	fmt.Printf("The first repeated frequency is %v\n", partTwo)
}
