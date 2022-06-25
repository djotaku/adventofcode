// Solution for Advent of Code Day 06 - Signals and Noise

package main

import "fmt"

func main() {
	var position_zero = make(map[rune]int)
	var position_one = make(map[rune]int)
	var position_two = make(map[rune]int)
	var position_three = make(map[rune]int)
	var position_four = make(map[rune]int)
	var position_five = make(map[rune]int)
	var position_six = make(map[rune]int)
	var position_seven = make(map[rune]int)
	counters := [8]map[rune]int{position_zero, position_one, position_two, position_three, position_four, position_five, position_six, position_seven}
	for position, character := range "helloooo" {
		counters[position][character]++
	}
	fmt.Printf("The value of 'a' is %d", position_one['o'])
}
