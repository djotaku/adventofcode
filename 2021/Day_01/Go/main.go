// Solution to Advent of Code 2021 Day 01: Sonar Sweep

package main

import (
	"aocinputs2021"
	"fmt"
)

// compareDepthsPart1 is a simple for loop, comparing each item with the next one to see if it's greater
func compareDepthsPart1(depthsList []int) int {
	count := 0
	currentDepth := depthsList[0]
	for index := range depthsList {
		if depthsList[index] > currentDepth {
			count += 1
		}
		currentDepth = depthsList[index]
	}
	return count
}

// compareDepthsPart2 uses the principle that if you want to know if a+b+c > b+c+d you just need to know if a < d
func compareDepthsPart2(depthsList []int) int {
	count := 0
	currentDepth := depthsList[0]
	for index := range depthsList {
		if index+3 < len(depthsList) {
			if depthsList[index+3] > currentDepth {
				count += 1
			}
			currentDepth = depthsList[index+1]
		}
	}
	return count
}

func main() {
	sonarDepths, err := aocinputs2021.MultipleLinesNumbers("/home/ermesa/Programming Projects/adventofcode/2021/Day_01/input.txt")
	if err != nil {
		print(err)
	}
	partOneAnswer := compareDepthsPart1(sonarDepths)
	fmt.Printf("The number of times the depth measurement increases is %d\n", partOneAnswer)
	partTwoAnswer := compareDepthsPart2(sonarDepths)
	fmt.Printf("The number of times the depth measurement increases when looking at triples is %d", partTwoAnswer)
}
