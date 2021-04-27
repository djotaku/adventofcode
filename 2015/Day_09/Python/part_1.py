"""Shortest Hamiltonian Walk aka Traveling Salesman who never goes back home."""

import re
from collections import defaultdict
from sys import maxsize
from itertools import permutations


def parse_connections(lines):
    regex = re.compile(r'(\w+) to (\w+) = (\d+)')
    hamilton_dict = defaultdict(list)
    for line in lines:
        destinations = re.findall(regex, line)
        value = {destinations[0][1]: destinations[0][2]}
        if destinations[0][0] not in hamilton_dict:
            hamilton_dict[destinations[0][0]] = [value]
        else:
            hamilton_dict[destinations[0][0]].append(value)
    return hamilton_dict


# implementation of traveling Salesman Problem
# adapted from https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
def travelling_salesman_problem(graph, s, V):
    # store all vertex apart from source vertex
    vertex = [i for i in range(V) if i != s]
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


if __name__ == "__main__":
    flight_connections = {"London": ["Dublin", "Belfast"], "Dublin": ["Belfast", "London"],
                          "Belfast": ["London", "Dublin"]}
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    V = 4
    print(travelling_salesman_problem(graph, s))
