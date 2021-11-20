//Solution to 2016 Day 04 -- Security Through Obscurity
package main

import (
	"adventofcode/2016/aocinputs"
	"fmt"
	"regexp"
	"sort"
	"strconv"
	"strings"
)

type characterFrequency struct {
	character string
	frequency int
}

func main() {
	roomList, err := aocinputs.MultipleLines("/home/ermesa/Programming Projects/adventofcode/2016/Day_04/input.txt")
	if err != nil {
		print(err)
	}
	sectorSum := 0
	for _, room := range roomList {
		sectorAndChecksumRegExp := regexp.MustCompile(`(\d+)\[(\w+)]`)
		encryptedRegExp := regexp.MustCompile(`(\w+)-`)
		sectorAndChecksum := sectorAndChecksumRegExp.FindStringSubmatch(room)
		sectorString := sectorAndChecksum[1]
		sector, _ := strconv.Atoi(sectorString)
		checksum := sectorAndChecksum[2]
		encryptedRoomBits := encryptedRegExp.FindAllString(room, -1)
		encryptedRoom := strings.Join(encryptedRoomBits, "")
		characterCounter := make(map[string]int)
		for _, character := range encryptedRoom {
			if string(character) != "-" {
				characterCounter[string(character)]++
			}
		}
		characterFrequencySlice := make([]characterFrequency, 29)
		for key, value := range characterCounter {
			characterFrequencySlice = append(characterFrequencySlice, characterFrequency{character: key, frequency: value})
		}
		// sorts the slice in place
		sort.SliceStable(characterFrequencySlice, func(i, j int) bool {
			if characterFrequencySlice[i].frequency != characterFrequencySlice[j].frequency {
				return characterFrequencySlice[i].frequency > characterFrequencySlice[j].frequency
			}
			return characterFrequencySlice[i].character < characterFrequencySlice[j].character
		})
		// final eval for part 1
		var checksumEval int
		checksumCharacters := strings.Split(checksum, "")
		for i := 0; i < 5; i++ {
			if characterFrequencySlice[i].character == checksumCharacters[i] {
				checksumEval++
			}
		}
		if checksumEval == 5 {
			sectorSum += sector
		}
	}
	fmt.Printf("The sum of all valid sectors is %d", sectorSum)
}
