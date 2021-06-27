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


def create_dictionary(sentences):
    regex = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\.')
    seating_dictionary = {}
    for sentence in sentences:
        matches = re.findall(regex, sentence)
        number = f'-{matches[0][2]}' if matches[0][1] == "lose" else matches[0][2]
        if matches[0][0] not in seating_dictionary:
            seating_dictionary[matches[0][0]] = {}
        seating_dictionary[matches[0][0]][matches[0][3]] = number
    return seating_dictionary


def create_graph(input_dictionary):
    index_dictionary = {index: key for index, key in enumerate(input_dictionary.keys())}
    matrix = []
    for number in range(len(index_dictionary)):
        temp_internal_list = []
        person = index_dictionary[number]
        for another_number in range(len(index_dictionary)):
            if another_number == number:
                temp_internal_list.append(0)
            else:
                temp_internal_list.append(int(input_dictionary[person][index_dictionary[another_number]]))
        temp_internal_list.append(0)
        matrix.append(temp_internal_list)
    final_zeroes = [0] * (len(index_dictionary) + 1)
    matrix.append(final_zeroes)
    return matrix


if __name__ == "__main__":
    guest_list = parse_input.input_per_line('../input.txt')
    guest_dictionary = create_dictionary(guest_list)
    guest_matrix = create_graph(guest_dictionary)
    final_happiness_level = happy_seating_genetic_algorithm(guest_matrix, 0, len(guest_matrix))
    print(f"The greatest happiness level with the best seating arrangement is {final_happiness_level}")