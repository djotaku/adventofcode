from itertools import permutations
import re
from sys import maxsize, path
path.insert(0, '../../input_parsing')
import parse_input


def happy_seating_genetic_algorithm(seating_matrix, starting_person, number_of_people):
    # store all vertex apart from source vertex
    vertex = [number for number in range(number_of_people) if number != starting_person]
    # store max happiness level
    max_happiness = 0
    total_permutations = permutations(vertex)
    for permutation in total_permutations:
        current_happiness = 0
        outer_array_index = starting_person
        for inner_array_index in permutation:
            current_happiness += seating_matrix[outer_array_index][inner_array_index]
            current_happiness += seating_matrix[inner_array_index][outer_array_index]
            outer_array_index = inner_array_index
        current_happiness += seating_matrix[outer_array_index][starting_person]
        current_happiness += seating_matrix[starting_person][outer_array_index]

        max_happiness = max(max_happiness, current_happiness)

    return max_happiness


def create_dictionary(sentence):
    regex = re.compile(r'(\w+).+(gain|lose) (\d+).+(\w+)\.')
    # regex = re.compile(r'(\w+)')
    # regex = re.compile(r'(gain|lose)')
    matches = re.findall(regex, sentence)
    print(f'{matches=}')
    number = -matches[0][2] if matches[0][1] == "lose" else matches[0][2]
    return {matches[0][0]: {matches[0][3]: number}}
