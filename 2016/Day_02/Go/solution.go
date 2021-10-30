//Solution to Advent of Code Day 02
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"github.com/deckarep/golang-set"
)

func main() {

	keypadPart1 := [3][3]int{{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9}}

	keypadPart2 := [5][5]string{{"0", "0", "1", "0", "0"},
		{"0", "2", "3", "4", "0"},
		{"5", "6", "7", "8", "9"},
		{"0", "A", "B", "C", "0"},
		{"0", "0", "D", "0", "0"}}

	validKeysPart1 := mapset.NewSet()
	validKeysPart1.Add("0,0")
	validKeysPart1.Add("0,1")
	validKeysPart1.Add("0,2")
	validKeysPart1.Add("1,0")
	validKeysPart1.Add("1,1")
	validKeysPart1.Add("1,2")
	validKeysPart1.Add("2,0")
	validKeysPart1.Add("2,1")
	validKeysPart1.Add("2,2")

	fmt.Printf("You thought the bathroom code was:")
	fmt.Printf("But the bathroom code turned out to be:")
}
