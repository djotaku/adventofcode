from itertools import combinations

with open("input", "r") as file:
    inputs = file.readlines()

potential_pairs = combinations(inputs, 3)

for pair in potential_pairs:
    if int(pair[0]) + int(pair[1]) + int(pair[2]) == 2020:
        print("Found the triplet")
        print(int(pair[0]) * int(pair[1]) * int(pair[2]))