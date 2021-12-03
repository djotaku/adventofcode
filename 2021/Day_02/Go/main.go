// Solution to Advent of Code 2021 Day 02: Dive!

package main

import (
	"aocinputs2021"
	"fmt"
	"strconv"
	"strings"
)

// simpleCommands takes a list of submarine commands and returns the product of the x and y values
func evaluateCommands(commands []string) (int, int) {
	horizontalPosition := 0
	verticalPositionPart1 := 0
	verticalPositionPart2 := 0
	aim := 0
	for _, command := range commands {
		commandSplit := strings.Fields(command)
		direction := commandSplit[0]
		magnitude, _ := strconv.Atoi(commandSplit[1])
		if direction == "forward" {
			horizontalPosition += magnitude
			verticalPositionPart2 += aim * magnitude
		} else if direction == "down" {
			verticalPositionPart1 += magnitude
			aim += magnitude
		} else { // direction is "up"
			verticalPositionPart1 -= magnitude
			aim -= magnitude
		}
	}
	partOneAnswer := horizontalPosition * verticalPositionPart1
	partTwoAnswer := horizontalPosition * verticalPositionPart2
	return partOneAnswer, partTwoAnswer
}

func main() {
	submarineCommands, err := aocinputs2021.MultipleLines("/home/ermesa/Programming Projects/adventofcode/2021/Day_02/input.txt")
	if err != nil {
		print(err)
	}
	partOneAnswer, partTwoAnswer := evaluateCommands(submarineCommands)
	fmt.Printf("The product calculation based on the naive instructions is %d. But the product based on the instructions once you've read the submarine manual is %d", partOneAnswer, partTwoAnswer)
}
