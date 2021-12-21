"""Solution for Advent of Code 2021 Day 15: Chiton using Dijkstra's Algorithm"""
from queue import PriorityQueue
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

        for neighbor in range(graph.vertices):
            if (
                    graph.edges[current_vertex][neighbor] != -1
                    and neighbor not in graph.visited
            ):
                old_cost = distance_cost_dictionary[neighbor]
                distance = graph.edges[current_vertex][neighbor]
                new_cost = distance_cost_dictionary[current_vertex] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    distance_cost_dictionary[neighbor] = new_cost
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
        numbers = [number for number in line]
        for number in numbers:
            this_grid[incrementing_number] = int(number)
            incrementing_number += 1
    return this_grid


def create_adjacency_grid(our_points: dict) -> dict:
    """For each point on the grid, creeate a dict entry (list) of other point we can get to.

     For part 1, at least, we cannot go diagonal.
     """
    this_adjacency_grid = {}
    for number in range(len(our_points.items())):
        above = None
        left = None
        right = None
        below = None
        # top row
        if 0 <= number <= 9:  # this needs to be adapted to the size of the input (make a function parameter)
            if number != 0:
                left = number - 1
            if number != 10:
                right = number + 1
            below = number + 10
        # bottom row
        elif 90 <= number <= 99:
            above = number - 10
            if number != 90:
                left = number - 1
            if number != 99:
                right = number + 1
        elif number % 10 == 0:
            right = number + 1
            below = number + 10
        elif number % 9 == 0:
            left = number - 1
            below = number + 10
        else:
            above = number - 10
            left = number - 1
            right = number + 1
            below = number + 10
        neighbors = [above, left, right, below]
        valid_neighbors = [neighbor for neighbor in neighbors if neighbor]
        this_adjacency_grid[number] = deepcopy(valid_neighbors)
    return this_adjacency_grid


if __name__ == "__main__":
    points = input_per_line("../input.txt")
    grid_of_points = create_grid(points)
    # print(grid_of_points)
    adjacency_grid = create_adjacency_grid(grid_of_points)
    print(adjacency_grid)
    size_of_graph = len(points)**2
    chiton_graph = Graph(size_of_graph)
    for key, value in adjacency_grid.items():
        for neighbor in value:
            # print(f"{key=}, {neighbor=}, {grid_of_points[neighbor]}")
            chiton_graph.add_edge(key, neighbor, grid_of_points[neighbor])
    dijkstra_solution = dijkstra(chiton_graph, 0)
    # print(dijkstra_solution)
    print(f"The lowest total risk to the bottom right position from the top left is:"
          f"{dijkstra_solution[99]}")
    # print(dijkstra(test_graph, 0))
