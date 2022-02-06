// Solution to Advent of Code Day 05 -- Do You Want to Play a Game

package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strconv"
)

// createHash returns a md5 hash of a string
func createHash(textToHash string) string {
	hash := md5.Sum([]byte(textToHash))
	return hex.EncodeToString(hash[:])
}

// validateHash returns true if this is a hash with 5 leading 0s
func validateHash(hashToCheck string) bool {
	for position, char := range hashToCheck {
		if position < 5 {
			if string(char) == "0" {
				continue
			} else {
				break
			}
		}
		if position == 5 {
			return true
		}
	}
	return false
}

// createDoorOnePassword takes in the input for this question and produces the password
func createDoorOnePassword(aocInput string) string {
	var password string
	numericalSuffix := 0
	for len(password) < 8 {
		testHash := createHash(aocInput + strconv.Itoa(numericalSuffix))
		//fmt.Println(testHash)
		if validateHash(testHash) {
			password += string([]rune(testHash)[5])
		}
		numericalSuffix++
	}
	return password
}

// createDoorTwoPassword takes in the aoc input and uses the new rules to produce the door password
func createDoorTwoPassword(aocInput string) string {
	var password [8]rune
	var locationCheck [8]bool
	numericalSuffix := 0
	for locationCheck[0] == false || locationCheck[1] == false || locationCheck[2] == false || locationCheck[3] == false || locationCheck[4] == false || locationCheck[5] == false || locationCheck[6] == false || locationCheck[7] == false {
		testHash := createHash(aocInput + strconv.Itoa(numericalSuffix))
		if validateHash(testHash) {
			probableLocation := string([]rune(testHash)[5])
			if probableLocation == "0" || probableLocation == "1" || probableLocation == "2" || probableLocation == "3" || probableLocation == "4" || probableLocation == "5" || probableLocation == "6" || probableLocation == "7" {
				location, _ := strconv.Atoi(probableLocation)
				character := []rune(testHash)[6]
				if locationCheck[location] == false {
					locationCheck[location] = true
					password[location] = character
				}

			}
		}
		numericalSuffix++
	}
	return string(password[:])
}

func main() {
	aocInput := "ugkcyxxp"
	doorOnePassword := createDoorOnePassword(aocInput)
	fmt.Printf("The password to door #1 is %s\n", doorOnePassword)
	doorTwoPassword := createDoorTwoPassword(aocInput)
	fmt.Printf("The password to door #2 is %s", doorTwoPassword)
}
