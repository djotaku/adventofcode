"""Solution for Advent of Code 2021 Day 15: Chiton using Dijkstra's Algorithm"""
import copy
from pprint import pprint
from queue import PriorityQueue
import heapq as heap
from collections import Counter
from copy import deepcopy


class Graph:
    """Implement a graph representing the chitons"""

    def __init__(self, num_of_vertices):
        self.vertices = num_of_vertices
        # basically equivalent to an "infinity" value for all edges to start with.
        self.edges = [[-1 for _ in range(num_of_vertices)] for _ in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        # self.edges[v][u] = weight


def dijkstra(graph, start_vertex):
    """Implement a Dijkstra algorithm over the graph.

    The result is the dictionary where the key is the vertex you want to know the distance to.
    """
    distance_cost_dictionary = {vertex: float('inf') for vertex in range(graph.vertices)}
    distance_cost_dictionary[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for current_neighbor in range(graph.vertices):
            if (
                    graph.edges[current_vertex][current_neighbor] != -1
                    and current_neighbor not in graph.visited
            ):
                old_cost = distance_cost_dictionary[current_neighbor]
                distance = graph.edges[current_vertex][current_neighbor]
                new_cost = distance_cost_dictionary[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, current_neighbor))
                    distance_cost_dictionary[current_neighbor] = new_cost
    return distance_cost_dictionary


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_grid(lines: list) -> dict:
    """Take in the lines of input from the problem and push to a dictionary with grid position as keys"""
    this_grid = {}
    incrementing_number = 0
    for line in lines:
        for number in line:
            this_grid[incrementing_number] = number
            incrementing_number += 1
    return this_grid


def create_adjacency_grid(our_points: dict, one_dimension: int) -> dict:
    """For each point on the grid, create a dict entry (list) of other point we can get to.

     For part 1, at least, we cannot go diagonal.
     """
    this_adjacency_grid = {}
    max_number = len(our_points.items()) - 1
    for number in range(len(our_points.items())):
        left = None
        right = None
        below = None
        # first number in a row
        if number % one_dimension == 0:
            right = number + 1
        elif (number + 1) % one_dimension == 0:
            left = number - 1
        else:
            left = number - 1
            if number + 1 <= max_number:
                right = number + 1
        above = number - one_dimension if (number - one_dimension) > -1 else None
        if (number + one_dimension) <= max_number:
            below = number + one_dimension
        neighbors = [above, left, right, below]
        valid_neighbors = [neighbor for neighbor in neighbors if neighbor is not None]
        this_adjacency_grid[number] = deepcopy(valid_neighbors)
    return this_adjacency_grid


def turn_input_into_grid_of_numbers(input_list: list) -> list:
    """Take our list which has lines of strings like '12345' and turn it into list of int lists."""
    fixed_list = []
    for line in input_list:
        temp_list = [int(character) for character in line]
        fixed_list.append(copy.deepcopy(temp_list))
    return fixed_list


def number_increase_and_wrap(number: int) -> int:
    """Increase the number or wrap it back to 1 if it goes past 9"""
    number += 1
    if number == 10:
        return 1
    else:
        return number


def increase_numbers(list_of_numbers: list) -> list:
    """Increase all the numbers. Wrap back to 1 if you go past 9."""
    increased_list = []
    for line in list_of_numbers:
        temp_list = [number_increase_and_wrap(number) for number in line]
        increased_list.append(copy.deepcopy(temp_list))
    return increased_list


def create_grid_row(list_1: list, list_2: list, list_3: list, list_4: list, list_5: list) -> list:
    """Basically create one row of grids"""
    grid_row = []
    for row_number, row in enumerate(list_1):
        temp_row = []
        for character in list_1[row_number]:
            temp_row.append(character)
        for character in list_2[row_number]:
            temp_row.append(character)
        for character in list_3[row_number]:
            temp_row.append(character)
        for character in list_4[row_number]:
            temp_row.append(character)
        for character in list_5[row_number]:
            temp_row.append(character)
        grid_row.append(copy.deepcopy(temp_row))
    return grid_row


def create_part_two_grid(original_input: list) -> tuple:
    """Take the input list and create the following (where 8 is the original):

    8 9 1 2 3
    9 1 2 3 4
    1 2 3 4 5
    2 3 4 5 6
    3 4 5 6 7
    """
    original_grid_plus_1 = increase_numbers(original_input)
    original_grid_plus_2 = increase_numbers(original_grid_plus_1)
    original_grid_plus_3 = increase_numbers(original_grid_plus_2)
    original_grid_plus_4 = increase_numbers(original_grid_plus_3)
    original_grid_plus_5 = increase_numbers(original_grid_plus_4)
    original_grid_plus_6 = increase_numbers(original_grid_plus_5)
    original_grid_plus_7 = increase_numbers(original_grid_plus_6)
    original_grid_plus_8 = increase_numbers(original_grid_plus_7)
    # a grid row is a repeating grid
    grid_row_0 = []
    grid_row_1 = []
    grid_row_2 = []
    grid_row_3 = []
    grid_row_4 = []
    grid_row_0 = create_grid_row(original_input, original_grid_plus_1, original_grid_plus_2, original_grid_plus_3,
                                 original_grid_plus_4)
    grid_row_1 = create_grid_row(original_grid_plus_1, original_grid_plus_2, original_grid_plus_3, original_grid_plus_4,
                                 original_grid_plus_5)
    grid_row_2 = create_grid_row(original_grid_plus_2, original_grid_plus_3, original_grid_plus_4, original_grid_plus_5,
                                 original_grid_plus_6)
    grid_row_3 = create_grid_row(original_grid_plus_3, original_grid_plus_4, original_grid_plus_5, original_grid_plus_6,
                                 original_grid_plus_7)
    grid_row_4 = create_grid_row(original_grid_plus_4, original_grid_plus_5, original_grid_plus_6, original_grid_plus_7,
                                 original_grid_plus_8)
    part_two_grid_dict = {}
    part_two_item_count = 0
    all_grids = [grid_row_0, grid_row_1, grid_row_2, grid_row_3, grid_row_4]
    for grid in all_grids:
        for line in grid:
            for number in line:
                part_two_grid_dict[part_two_item_count] = number
                part_two_item_count += 1
    return part_two_grid_dict, len(grid_row_0[0])


if __name__ == "__main__":
    points = input_per_line("../input.txt")
    integer_points = turn_input_into_grid_of_numbers(points)
    grid_of_points = create_grid(integer_points)
    # print(grid_of_points)
    size_of_one_side = len(points)
    adjacency_grid = create_adjacency_grid(grid_of_points, size_of_one_side)
    # print(adjacency_grid)
    size_of_graph = size_of_one_side ** 2
    chiton_graph = Graph(size_of_graph)
    for key, value in adjacency_grid.items():
        for this_neighbor in value:
            # print(f"{key=}, {neighbor=}, {grid_of_points[neighbor]}")
            chiton_graph.add_edge(key, this_neighbor, grid_of_points[this_neighbor])
    dijkstra_solution = dijkstra(chiton_graph, 0)

    # print(f"{dijkstra_solution=}")
    print(f"The lowest total risk to the bottom right position from the top left is:"
          f"{dijkstra_solution[size_of_graph-1]}")  # this part has to be changed between test input and real input
    # print(chiton_graph.visited)
    # Part 2
    part_two_grid, part_two_size_of_one_side = create_part_two_grid(integer_points)
    # print(f"{part_two_grid=}")
    # print(f"{part_two_size_of_one_side=}")
    part_two_adjacency_grid = create_adjacency_grid(part_two_grid, part_two_size_of_one_side)
    # print(f"{part_two_adjacency_grid}")
    part_two_size_of_graph = part_two_size_of_one_side**2
    part_two_chiton_graph = Graph(part_two_size_of_graph)
    for key, value in part_two_adjacency_grid.items():
        for this_neighbor in value:
            # print(f"{key=}, {value=}, {this_neighbor=}, {part_two_grid[this_neighbor]=}")
            part_two_chiton_graph.add_edge(key, this_neighbor, part_two_grid[this_neighbor])
    part_two_dijkstra_solution = dijkstra(part_two_chiton_graph, 0)
    print(f"The lowest total risk to the bottom right position from the top left in part 2 is:"
          f"{part_two_dijkstra_solution[part_two_size_of_graph - 1]}")
