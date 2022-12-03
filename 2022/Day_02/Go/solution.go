// Solution to AoC 2022 Day 02 - Rock Paper Scissors

package main

import (
	"bufio"
	"fmt"
	"os"
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

// rock=1, paper=2, scissors=3
// win=6, tie=3, loss=0
func main() {
	strategyGuide, _ := MultipleLines("../input.txt")
	SCORES := map[string]map[string]int{
		"rock": {
			"rock":     4,
			"paper":    8,
			"scissors": 3,
		},
		"paper": {
			"rock":     1,
			"paper":    5,
			"scissors": 9,
		},
		"scissors": {
			"rock":     7,
			"paper":    2,
			"scissors": 6,
		},
	}
	opponentShape := map[string]string{
		"A": "rock",
		"B": "paper",
		"C": "scissors",
	}
	partOneShape := map[string]string{
		"X": "rock",
		"Y": "paper",
		"Z": "scissors",
	}
	// part 2 x=lose, y=tie, z=win
	partTwoMap := map[string]map[string]string{
		"rock": {
			"X": "scissors",
			"Y": "rock",
			"Z": "paper",
		},
		"paper": {
			"X": "rock",
			"Y": "paper",
			"Z": "scissors",
		},
		"scissors": {
			"X": "paper",
			"Y": "scissors",
			"Z": "rock",
		},
	}
	partOneSum := 0
	partTwoSum := 0
	for _, suggestedMove := range strategyGuide {
		shapes := strings.Fields(suggestedMove)
		partOneSum += SCORES[opponentShape[shapes[0]]][partOneShape[shapes[1]]]
		partTwoSum += SCORES[opponentShape[shapes[0]]][partTwoMap[opponentShape[shapes[0]]][shapes[1]]]
	}
	fmt.Printf("Score for part one is %d\n", partOneSum)
	fmt.Printf("Score for part two is %d\n", partTwoSum)
}
