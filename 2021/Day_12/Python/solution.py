"""Solution for Advent of Code 2021 Day 12: Passage Pathing"""
from collections import defaultdict
from copy import deepcopy
import logging
logger_12 = logging.getLogger("Day_12")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def create_graph(graph_connection_input: list) -> dict:
    """Take in list of connections and create the dictionary."""
    graph = defaultdict(list)
    for line in graph_connection_input:
        nodes = line.split("-")
        if nodes[0] != "end":
            graph[nodes[0]].append(nodes[1])
        if nodes[0] != "start" and nodes[1] != "end":
            graph[nodes[1]].append(nodes[0])
    return graph


path = []


def traverse_graph(visited, graph, can_revisit=True):
    """Do a depth-first search of the graph.

    Only visit small nodes once.

    Stop at end.
    """
    # check if we've reached "end" to end the recursion
    if visited[-1] == "end":
        return 1
    return sum(
        traverse_graph(
            visited + [next_node],
            graph,
            can_revisit and not (next_node.islower() and next_node in visited)
        )
        for next_node in graph[visited[-1]]
        if next_node not in visited or next_node.isupper() or can_revisit
        )


if __name__ == "__main__":
    graph_implementation = input_per_line("../input.txt")
    the_graph = create_graph(graph_implementation)
    logger_12.debug(f"{the_graph}")
    visited_nodes = ["start"]
    part_1 = traverse_graph(visited_nodes, the_graph, False)
    print(f"There are {part_1} paths.")
