"""Shortest Hamiltonian Walk aka Traveling Salesman who never goes back home."""


from collections import defaultdict
from itertools import permutations
import re
from sys import maxsize


def parse_connections(lines):
    regex = re.compile(r'(\w+) to (\w+) = (\d+)')
    hamilton_dict = defaultdict(list)
    for line in lines:
        destinations = re.findall(regex, line)
        hamilton_dict[destinations[0][0]].append({destinations[0][1]: destinations[0][2]})
        hamilton_dict[destinations[0][1]].append({destinations[0][0]: destinations[0][2]})
    return hamilton_dict


# implementation of traveling Salesman Problem
# adapted from https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def travelling_salesman_problem(graph, starting_city: int, number_of_cities):
    """Solve Traveling Salesman Problem Naive Method.

    If you want to do shortest Hamiltonian Walk, you need
    to have an extra row and column of 0s at the end and bottom.
    And you have to have your number of vertices 1 more than the real number.

    :param graph: A matrix of distances between cities. Add an extra row and column of 0s for shortest Hamilton Walk.
    :param starting_city: Should be an the index of one of the cities.
    :param number_of_cities: The number of cities to visit. Add an extra one for Shortest Hamilton Walk.
    """
    # store all vertex apart from source vertex
    vertex = [number for number in range(number_of_cities) if number != starting_city]
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
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
        min_path = min(min_path, current_path_weight)

    return min_path


if __name__ == "__main__":
    pass
