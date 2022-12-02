// Solution to Advent of Code 2022 Day 01 - Calorie Counting

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// ParseElves returns the input file if it contains multiple lines of text
func ParseElves(fileName string) ([]int, error) {
	inputSlice := make([]int, 0)
	file, err := os.Open(fileName)
	if err != nil {
		return inputSlice, err
	}
	scanner := bufio.NewScanner(file)
	calorieSum := 0
	for scanner.Scan() {
		thisNumber, _ := strconv.Atoi(scanner.Text())
		// fmt.Printf("Number in loop: %d\n", thisNumber)
		if thisNumber != 0 {
			// fmt.Printf("not a 0!")
			calorieSum += thisNumber
			// fmt.Printf("calorieSum %d\n", calorieSum)
		} else {
			inputSlice = append(inputSlice, calorieSum)
			calorieSum = 0
		}
	}
	err = file.Close()
	if err != nil {
		return inputSlice, err
	}
	return inputSlice, nil
}

func main() {
	elfCalories, err := ParseElves("../input.txt")
	if err != nil {
		// fmt.Printf("Error%v\n", err)
	}
	// fmt.Printf("Elf Calories: %v\n", elfCalories)
	maxCalories := [3]int{0, 0, 0}
	for _, elfCalorieTotal := range elfCalories {
		if elfCalorieTotal > maxCalories[0] {
			temp := maxCalories[0]
			maxCalories[0] = elfCalorieTotal
			tempTwo := maxCalories[1]
			maxCalories[1] = temp
			maxCalories[2] = tempTwo
		} else if elfCalorieTotal > maxCalories[1] {
			temp := maxCalories[1]
			maxCalories[1] = elfCalorieTotal
			maxCalories[2] = temp
		} else if elfCalorieTotal > maxCalories[2] {
			maxCalories[2] = elfCalorieTotal
		}
	}
	fmt.Printf("The elf with the most calories has food worth %d calories\n", maxCalories[0])
	partTwoTotal := maxCalories[0] + maxCalories[1] + maxCalories[2]
	fmt.Printf("The elves with the top 3 most calories have food worth %d calories", partTwoTotal)

}
