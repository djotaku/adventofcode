// Solution to Advent of Code 2021 Day 01: Sonar Sweep

package main

import (
	"aocinputs2021"
	"fmt"
)

func compareDepthsPart1(depthsList []int) int {
	count := 0
	currentDepth := depthsList[0]
	for index, _ := range depthsList {
		if depthsList[index] > currentDepth {
			count += 1
		}
		currentDepth = depthsList[index]
	}
	return count
}

func main() {
	sonarDepths, err := aocinputs2021.MultipleLinesNumbers("/home/ermesa/Programming Projects/adventofcode/2021/Day_01/input.txt")
	if err != nil {
		print(err)
	}
	partOneAnswer := compareDepthsPart1(sonarDepths)
	fmt.Printf("The number of times the depth measurement increases is %d", partOneAnswer)
}
