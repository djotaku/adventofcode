"""Solution for Advent of Code 2021 Day 12: Passage Pathing"""
import logging
logger_12 = logging.getLogger("Day_12")
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_connected_nodes(current_node: int, node_graph: list) -> list:
    """Figure out where you can get to from here.

    param current_node: Your current location as the index of where it is on the graph.
    param node_graph: A list of lists that expresses where you can go next.
    :return: List of nodes you can get to from here.
    """
    return [row_number for row_number, row in enumerate(node_graph) if row[current_node] == 1]


def find_paths(node_graph: list) -> int:
    """Find all paths through the cave system.

    param node_graph: A list of lists that expresses all the connections between nodes
    :return: The number of paths through the system
    """
    # designed with the assumption that start is index 0 and end is the final index.
    # find index that represents end
    end = len(node_graph[0]) - 1
    all_paths = set()
    paths_to_check = []
    start_nodes = find_connected_nodes(0, node_graph)
    for node in start_nodes:
        pass


def find_paths_recursive(node_graph: list, current_node: int):
    paths = []
    if current_node == len(node_graph[0]) - 1:  # end
        return str(len(node_graph) - 1)
    else:
        connected_nodes = find_connected_nodes(current_node, node_graph)
        logger_12.debug(f"{connected_nodes}")
        for node in connected_nodes:
            logger_12.debug(f"{node}")
            temp_path = []
            next_nodes = find_connected_nodes(node, node_graph)
            for next_node in next_nodes:
                temp_path.append(find_paths_recursive(node_graph, next_node))
                logger_12.debug(f"{temp_path=}")
    return paths


if __name__ == "__main__":
    first_sample_graph = [
        [0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]
    ]
    print("HI")
    print(find_paths_recursive(first_sample_graph, 0))
