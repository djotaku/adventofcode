from itertools import permutations
import re
from sys import maxsize, path
path.insert(0, '../../input_parsing')
import parse_input


def happy_seating_arrangement(graph, starting_person: int, number_of_people):
    """For AoC implementing LONGEST path.

    :param graph: A matrix of distances between cities. Add an extra row and column of 0s for shortest Hamilton Walk.
    :param starting_person: Should be an the index of one of the cities.
    :param number_of_people: The number of cities to visit. Add an extra one for Shortest Hamilton Walk.
    """
    # store all vertex apart from source vertex
    vertex = [number for number in range(number_of_people) if number != starting_person]
    # store minimum weight Hamiltonian Cycle
    max_path = 0
    next_permutation = permutations(vertex)
    for permutation in next_permutation:

        # store current Path weight(cost)
        current_path_weight = 0

        # compute current path weight
        outer_array_index = starting_person
        for inner_array_index in permutation:
            current_path_weight += graph[outer_array_index][inner_array_index]
            outer_array_index = inner_array_index
        current_path_weight += graph[outer_array_index][starting_person]

        # update minimum
        max_path = max(max_path, current_path_weight)

    return max_path


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

        max_happiness = max(max_happiness, current_happiness)

    return max_happiness
