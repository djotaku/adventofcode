"""Solution to Aoc 2022 Day 03 - Rucksack Reorganization."""

def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

if __name__ == "__main__":
    rucksacks = input_per_line("../input.txt")
    priorities = {"a": 1, "b": 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13,
                  "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v":22, "w": 23, "x": 24,
                  "y":25, "z": 26, "A": 27, "B": 28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36,
                  "K":37, "L":38, "M":39, "N":40, "O": 41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U": 47, "V":48,
                  "W":49, "X":50, "Y":51, "Z":52}
    unique_letters = []
    for rucksack in rucksacks:
        string_length = len(rucksack)
        left_set: set = set()
        right_set: set = set()
        for index, item in enumerate(rucksack):
            if index < string_length/2:
                left_set.add(item)
            else:
                right_set.add(item)
        unique_letter = left_set.intersection(right_set)
        unique_letters.append(unique_letter.pop())
    unique_values = [priorities[letter] for letter in unique_letters]
    print(f"The sum of priorities is {sum(unique_values)}")