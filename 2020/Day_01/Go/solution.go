// Package main solves AoC 2020 Day 01: Report Repair
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// MultipleLinesNumbers returns the input file if it contains multiple lines of text
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

func findNumber(number int, numberList []int) bool {
	for _, currentNumber := range numberList {
		if number == currentNumber {
			return true
		}
	}
	return false
}

func main() {
	expenseReportEntries, err := MultipleLinesNumbers("../input.txt")
	if err != nil {
		fmt.Println("Couldn't find input.txt")
	}
	for _, numberToCheck := range expenseReportEntries {
		difference := 2020 - numberToCheck
		if findNumber(difference, expenseReportEntries) {
			fmt.Printf("The two numbers that sum to 2020 in the expense report are %d and %d\n", numberToCheck, difference)
			fmt.Printf("Multiplied together, the product is %d\n", numberToCheck*difference)
			break
		}
	}
}
