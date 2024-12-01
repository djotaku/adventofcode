// Solution to Advent of Code 2024 Day 01 - Historian Hysteria

package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

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

func main() {
	lists, err := MultipleLines("../input.txt")
	if err != nil {
		fmt.Printf("Error%v\n", err)
	}
	var leftSide []float64
	var rightSide []float64
	// split the left and right and convert them to ints.
	for _, line := range lists {
		temp := strings.Fields(line)
		left, _ := strconv.ParseFloat(temp[0], 64)
		right, _ := strconv.ParseFloat(temp[1], 64)
		leftSide = append(leftSide, left)
		rightSide = append(rightSide, right)
	}
	// Take advantage of the new slice sorting in Go. It sorts in place
	slices.Sort(leftSide)
	slices.Sort(rightSide)

	// a new slice to hold the differences
	var diff []float64

	for index, value := range leftSide {
		diff = append(diff, math.Abs(value-rightSide[index]))
	}

	var sum float64

	for _, value := range diff {
		sum += value
	}

	fmt.Printf("The total distance between the lists is %f\n", sum)

	// map to hold a count of values in the right side
	var counter = make(map[float64]int)

	for _, number := range rightSide {
		counter[number] += 1
	}

	var product []float64

	for _, number := range leftSide {
		product = append(product, number*float64(counter[number]))
	}

	var productSum float64

	for _, number := range product {
		productSum += number
	}

	fmt.Printf("The simlarity score is %f", productSum)
}
