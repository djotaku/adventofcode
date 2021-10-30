//Solution to Advent of Code Day 02
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"github.com/deckarep/golang-set"
	"strconv"
)

var keypadPart1 = [3][3]string{{"1", "2", "3"},
	{"4", "5", "6"},
	{"7", "8", "9"}}

var keypadPart2 = [5][5]string{{"0", "0", "1", "0", "0"},
	{"0", "2", "3", "4", "0"},
	{"5", "6", "7", "8", "9"},
	{"0", "A", "B", "C", "0"},
	{"0", "0", "D", "0", "0"}}

// I could have done this with a map instead
var validKeysPart1 = mapset.NewSet()
var validKeysPart2 = mapset.NewSet()

func findNextKey(outerMatrix int, innerMatrix int, directionsThisKey string, part int) (string, int, int) {
	thisRoundOuterMatrix := outerMatrix
	thisRoundInnerMatrix := innerMatrix
	for _, char := range directionsThisKey {
		if char == 'U' {
			newOuterMatrix := thisRoundOuterMatrix - 1
			pairToCheck := strconv.Itoa(newOuterMatrix) + "," + strconv.Itoa(thisRoundInnerMatrix)
			if part == 1 {
				if validKeysPart1.Contains(pairToCheck) {
					thisRoundOuterMatrix = newOuterMatrix
				}
			} else {
				if validKeysPart2.Contains(pairToCheck) {
					thisRoundOuterMatrix = newOuterMatrix
				}
			}
		}
		if char == 'D' {
			newOuterMatrix := thisRoundOuterMatrix + 1
			pairToCheck := strconv.Itoa(newOuterMatrix) + "," + strconv.Itoa(thisRoundInnerMatrix)
			if part == 1 {
				if validKeysPart1.Contains(pairToCheck) {
					thisRoundOuterMatrix = newOuterMatrix
				}
			} else {
				if validKeysPart2.Contains(pairToCheck) {
					thisRoundOuterMatrix = newOuterMatrix
				}
			}
		}
		if char == 'L' {
			newInnerMatrix := thisRoundInnerMatrix - 1
			pairToCheck := strconv.Itoa(thisRoundOuterMatrix) + "," + strconv.Itoa(newInnerMatrix)
			if part == 1 {
				if validKeysPart1.Contains(pairToCheck) {
					thisRoundInnerMatrix = newInnerMatrix
				}
			} else {
				if validKeysPart2.Contains(pairToCheck) {
					thisRoundInnerMatrix = newInnerMatrix
				}
			}
		}
		if char == 'R' {
			newInnerMatrix := thisRoundInnerMatrix + 1
			pairToCheck := strconv.Itoa(thisRoundOuterMatrix) + "," + strconv.Itoa(newInnerMatrix)
			if part == 1 {
				if validKeysPart1.Contains(pairToCheck) {
					thisRoundInnerMatrix = newInnerMatrix
				}
			} else {
				if validKeysPart2.Contains(pairToCheck) {
					thisRoundInnerMatrix = newInnerMatrix
				}
			}
		}
	}
	if part == 1 {
		return keypadPart1[thisRoundOuterMatrix][thisRoundInnerMatrix], thisRoundOuterMatrix, thisRoundInnerMatrix
	}
	return keypadPart2[thisRoundOuterMatrix][thisRoundInnerMatrix], thisRoundOuterMatrix, thisRoundInnerMatrix
}

func main() {

	validKeysPart1.Add("0,0")
	validKeysPart1.Add("0,1")
	validKeysPart1.Add("0,2")
	validKeysPart1.Add("1,0")
	validKeysPart1.Add("1,1")
	validKeysPart1.Add("1,2")
	validKeysPart1.Add("2,0")
	validKeysPart1.Add("2,1")
	validKeysPart1.Add("2,2")

	validKeysPart2.Add("0,2")
	validKeysPart2.Add("1,1")
	validKeysPart2.Add("1,2")
	validKeysPart2.Add("1,3")
	validKeysPart2.Add("2,0")
	validKeysPart2.Add("2,1")
	validKeysPart2.Add("2,2")
	validKeysPart2.Add("2,3")
	validKeysPart2.Add("2,4")
	validKeysPart2.Add("3,1")
	validKeysPart2.Add("3,2")
	validKeysPart2.Add("3,3")
	validKeysPart2.Add("4,2")

	keypadInstructions, err := aocinputs.MultipleLines("/home/ermesa/Programming Projects/adventofcode/2016/Day_02/input.txt")
	if err != nil {
		print(err)
	}
	//keypadInstructions := []string{"ULL", "RRDDD", "LURDL", "UUUD"}
	partOneInnerMatrix := 1
	partOneOuterMatrix := 1
	var partOneCode string
	var partialAnswer string
	for _, instruction := range keypadInstructions {
		partialAnswer, partOneOuterMatrix, partOneInnerMatrix = findNextKey(partOneOuterMatrix, partOneInnerMatrix, instruction, 1)
		partOneCode += partialAnswer
	}
	partTwoInnerMatrix := 0
	partTwoOuterMatrix := 2
	var partTwoCode string
	for _, instruction := range keypadInstructions {
		partialAnswer, partTwoOuterMatrix, partTwoInnerMatrix = findNextKey(partTwoOuterMatrix, partTwoInnerMatrix, instruction, 2)
		partTwoCode += partialAnswer
	}
	fmt.Printf("You thought the bathroom code was: %s\n", partOneCode)
	fmt.Printf("But the bathroom code turned out to be: %s", partTwoCode)
}
