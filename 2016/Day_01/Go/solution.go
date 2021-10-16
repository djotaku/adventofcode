// Solution to Advent of Code 2016 Day 01
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"math"
	"regexp"
	"strconv"
	"strings"
)

func main() {

	direction := [2]int{0, 1}
	myLocation := [2]int{0, 0}
	visitedLocations := map[string]float64{"0,0": 1}
	var partTwoLocation [2]int
	continueToLookForDuplicates := true

	directionInput, err := aocinputs.OneLine("/home/ermesa/Programming Projects/adventofcode/2016/Day_01/input.txt")
	if err != nil {
		print(err)
	}
	directions := strings.Split(directionInput, ",")
	for _, value := range directions {
		re := regexp.MustCompile(`(\w)(\d+)`)
		matches := re.FindStringSubmatch(value)
		if matches[1] == "L" {
			tempX := direction[0]
			direction[0] = -direction[1]
			direction[1] = tempX
		} else {
			tempX := direction[0]
			direction[0] = direction[1]
			direction[1] = -tempX
		}
		distanceToTravel, _ := strconv.Atoi(matches[2])
		for step := 0; step < distanceToTravel; step++ {
			myLocation[0] += direction[0]
			myLocation[1] += direction[1]
			locationAsString := strconv.Itoa(myLocation[0]) + "," + strconv.Itoa(myLocation[1])
			if visitedLocations[locationAsString] == 1 && continueToLookForDuplicates {
				partTwoLocation[0] = myLocation[0]
				partTwoLocation[1] = myLocation[1]
				continueToLookForDuplicates = false
			} else {
				visitedLocations[locationAsString] = 1
			}
		}
	}

	partOneAnswer := math.Abs(float64(myLocation[0])) + math.Abs(float64(myLocation[1]))
	partTwoAnswer := math.Abs(float64(partTwoLocation[0])) + math.Abs(float64(partTwoLocation[1]))
	fmt.Printf("According to part 1's instructions. Easter Bunny HQ is %f blocks away.\n", partOneAnswer)
	fmt.Printf("According to part 2's instructions. Easter Bunny HQ is %f blocks away.\n", partTwoAnswer)
}
