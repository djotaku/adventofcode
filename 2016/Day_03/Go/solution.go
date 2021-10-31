//Advent of Code 2016 Day 3 Solution
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"strconv"
	"strings"
)

// isATriangle determines if the triples are sides of a triangle and returns 1 if they are
func isATriangle(sideA int, sideB int, sideC int) int {
	if sideA+sideB > sideC && sideB+sideC > sideA && sideA+sideC > sideB {
		return 1
	} else {
		return 0
	}
}

func main() {
	potentialTriangles, err := aocinputs.MultipleLines("/home/ermesa/Programming Projects/adventofcode/2016/Day_03/input.txt")
	if err != nil {
		print(err)
	}

	partOneCount := 0

	for _, triple := range potentialTriangles {
		// usefulTriple := strings.Split(triple, " ")
		usefulTriple := strings.Fields(triple)
		sideA, _ := strconv.Atoi(usefulTriple[0])
		sideB, _ := strconv.Atoi(usefulTriple[1])
		sideC, _ := strconv.Atoi(usefulTriple[2])
		partOneCount += isATriangle(sideA, sideB, sideC)
	}

	fmt.Printf("If you look at rows, we have: %d triangles on the list.\n", partOneCount)
}
