// Solution for Advent of Code Day 06 - Signals and Noise

package main

import (
	"bufio"
	"fmt"
	"os"
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

// FindMinMaxLetter finds the letter that appears most often in the map
func FindMinMaxLetter(positionMap map[rune]int) (rune, rune) {
	maxVal := 0
	minVal := 999999
	var maxRune rune
	var minRune rune
	for key, value := range positionMap {
		if value > maxVal {
			maxVal = value
			maxRune = key
		}
		if value < minVal {
			minVal = value
			minRune = key
		}
	}
	return maxRune, minRune
}

func main() {
	var positionZero = make(map[rune]int)
	var positionOne = make(map[rune]int)
	var positionTwo = make(map[rune]int)
	var positionThree = make(map[rune]int)
	var positionFour = make(map[rune]int)
	var positionFive = make(map[rune]int)
	var positionSix = make(map[rune]int)
	var positionSeven = make(map[rune]int)
	counters := [8]map[rune]int{positionZero, positionOne, positionTwo, positionThree, positionFour, positionFive, positionSix, positionSeven}
	ourInput, _ := MultipleLines("/home/ermesa/Programming Projects/adventofcode/2016/Day_06/input.txt")
	for _, word := range ourInput {
		for position, character := range word {
			counters[position][character]++
		}
	}
	outputPartOne := ""
	outputPartTwo := ""
	fmt.Println("The error-corrected message is:")
	for _, value := range counters {
		maxOutput, minOutput := FindMinMaxLetter(value)
		outputPartOne += string(maxOutput)
		outputPartTwo += string(minOutput)
	}
	fmt.Println("For part one:", outputPartOne)
	fmt.Println("For part two: ", outputPartTwo)
}
