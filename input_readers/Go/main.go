// Package aocinputs2021 reads Advent of Code inputs
package aocinputs

import (
	"bufio"
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

// MultipleLines returns the input file if it contains multiple lines of text
func MultipleLines(fileName string) ([]string, error) {
	inputSlice := make([]string, 0)
	file, err := os.Open(fileName)
	if err != nil {
		return inputSlice, err
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		inputSlice = append(inputSlice, scanner.Text())
	}
	err = file.Close()
	if err != nil {
		return inputSlice, err
	}
	return inputSlice, nil
}

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
