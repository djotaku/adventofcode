// Advent of Code 2015 Day 01 - Not Quite Lisp
package main

import (
	"bufio"
	"fmt"
	"os"
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

// ParseParenthesis returns the final floor and the position when Santa enters the basement
func ParseParenthesis(parens string) (int, int) {
	var finalFloor = 0
	var positionBasement = 0
	var searchForFinalFloor = true
	for parenthesisPosition, parenthesis := range parens {
		if parenthesis == '(' {
			finalFloor += 1
		} else {
			finalFloor -= 1
		}
		if finalFloor == -1 && searchForFinalFloor {
			positionBasement = parenthesisPosition + 1
			searchForFinalFloor = false
		}
	}
	return finalFloor, positionBasement
}

func main() {
	floorDirections, err := OneLine("../input.txt")
	if err != nil {
		print(err)
	}
	partOne, partTwo := ParseParenthesis(floorDirections)
	fmt.Printf("Santa ends up at %d\n", partOne)
	fmt.Printf("The first time Santa enters the basement is on instruction %d", partTwo)
}
