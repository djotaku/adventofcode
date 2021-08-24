from itertools import combinations

with open("input", "r") as file:
    inputs = file.readlines()

potential_pairs = combinations(inputs, 2)

for pair in potential_pairs:
    if int(pair[0]) + int(pair[1]) == 2020:
        print("Found the pair")
        print(int(pair[0]) * int(pair[1]))