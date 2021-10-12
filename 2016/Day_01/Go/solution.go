// Solution to Advent of Code 2016 Day 01
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"strings"
)

func main() {

	direction := [2]float64{0, 1}
	myLocation := [2]float64{0, 0}
	visitedLocations := map[string]float64{"0,0": 1}
	continueToLookForDuplicates := true

	directionInput, err := aocinputs.OneLine("../input.txt")
	if err != nil {
		print(err)
	}
	directions := strings.Split(directionInput, ",")
	for _, value := range directions {
		// start https://pkg.go.dev/regexp when you get back to this
	}

	fmt.Println("hi")
}
