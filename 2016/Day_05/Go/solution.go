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

func main() {
	doorOnePassword := createDoorOnePassword("ugkcyxxp")
	fmt.Printf("The password to door #1 is %s", doorOnePassword)
}
