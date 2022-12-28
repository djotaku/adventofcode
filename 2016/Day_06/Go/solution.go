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

// FindMaxLetter finds the letter that appears most often in the map
func FindMaxLetter(positionMap map[rune]int) rune {
	maxVal := 0
	var returnRune rune
	for key, value := range positionMap {
		if value > maxVal {
			maxVal = value
			returnRune = key
		}
	}
	return returnRune
}

func main() {
	var position_zero = make(map[rune]int)
	var position_one = make(map[rune]int)
	var position_two = make(map[rune]int)
	var position_three = make(map[rune]int)
	var position_four = make(map[rune]int)
	var position_five = make(map[rune]int)
	var position_six = make(map[rune]int)
	var position_seven = make(map[rune]int)
	counters := [8]map[rune]int{position_zero, position_one, position_two, position_three, position_four, position_five, position_six, position_seven}
	ourInput, _ := MultipleLines("/home/ermesa/Programming Projects/adventofcode/2016/Day_06/input.txt")
	for _, word := range ourInput {
		for position, character := range word {
			counters[position][character]++
		}
	}
	fmt.Println("The error-corrected message is:")
	for _, value := range counters {
		output := string(FindMaxLetter(value))
		fmt.Print(output)
	}
	fmt.Println("")
}
