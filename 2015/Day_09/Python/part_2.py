"""Longest Hamiltonian Walk aka Traveling Salesman who never goes back home."""


from itertools import permutations
import re
from sys import maxsize, path
path.insert(0, '../../input_parsing')
import parse_input


def parse_connections(lines):
    regex = re.compile(r'(\w+) to (\w+) = (\d+)')
    hamilton_dict = {}
    for line in lines:
        destinations = re.findall(regex, line)
        if destinations[0][0] not in hamilton_dict:
            hamilton_dict[destinations[0][0]] = {}
        hamilton_dict[destinations[0][0]][destinations[0][1]] = destinations[0][2]
        if destinations[0][1] not in hamilton_dict:
            hamilton_dict[destinations[0][1]] = {}
        hamilton_dict[destinations[0][1]][destinations[0][0]] = destinations[0][2]
    return hamilton_dict


def create_matrix(city_dict):
    # first create a number to city_dict for making the graph
    index_dictionary = {index: key for index, key in enumerate(city_dict.keys())}
    matrix = []
    for number in range(len(index_dictionary)):
        temp_internal_list = []
        current_city = index_dictionary[number]
        for another_number in range(len(index_dictionary)):
            if another_number == number:
                temp_internal_list.append(0)
            else:
                temp_internal_list.append(int(city_dict[current_city][index_dictionary[another_number]]))
        temp_internal_list.append(0)
        matrix.append(temp_internal_list)
    final_zeroes = [0] * (len(index_dictionary) + 1)
    matrix.append(final_zeroes)
    return matrix


# implementation of traveling Salesman Problem
# adapted from https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def travelling_salesman_problem(graph, starting_city: int, number_of_cities):
    """For AoC implementing LONGEST path.

    :param graph: A matrix of distances between cities. Add an extra row and column of 0s for shortest Hamilton Walk.
    :param starting_city: Should be an the index of one of the cities.
    :param number_of_cities: The number of cities to visit. Add an extra one for Shortest Hamilton Walk.
    """
    # store all vertex apart from source vertex
    vertex = [number for number in range(number_of_cities) if number != starting_city]
    # store minimum weight Hamiltonian Cycle
    max_path = 0
    next_permutation = permutations(vertex)
    for permutation in next_permutation:

        # store current Path weight(cost)
        current_path_weight = 0

        # compute current path weight
        outer_array_index = starting_city
        for inner_array_index in permutation:
            current_path_weight += graph[outer_array_index][inner_array_index]
            outer_array_index = inner_array_index
        current_path_weight += graph[outer_array_index][starting_city]

        # update minimum
        max_path = max(max_path, current_path_weight)

    return max_path


if __name__ == "__main__":
    city_list = parse_input.input_per_line('../input.txt')
    city_connections = parse_connections(city_list)
    city_matrix = create_matrix(city_connections)
    starting_city = 0
    distance = travelling_salesman_problem(city_matrix, starting_city, len(city_matrix))
    print(f"The distance of the longest route is {distance}")
