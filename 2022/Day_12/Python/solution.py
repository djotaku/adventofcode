"""Solution to AoC 2022 Day 12 - Hill Climbing Algorithm."""
from collections import defaultdict, deque


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def text_to_grid(text_map: list) -> (dict, int, int):
    """Take in a list of items that need to be parsed into a dictionary where each set of keys is a coordinate.

    Return a dictionary representation of the map.
    """
    grid_map = defaultdict(str)
    max_y = len(text_map)
    max_x = len(text_map[0])
    for y, line in enumerate(text_map):
        for x, letter in enumerate(line):
            grid_map[(x, y)] = letter
    return grid_map, max_x, max_y


def find_start_and_end(grid_map: dict) -> tuple:
    """Find the coordinates of the start and end points."""
    start_coordinate = None
    end_coordinate = None
    for key, value in grid_map.items():
        if value == "E":
            end_coordinate = key
        elif value == "S":
            start_coordinate = key
    return start_coordinate, end_coordinate


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class QueueNode:
    """A data structure for queue used in BFS"""

    def __init__(self, point: Point, distance: int):
        self.point = point
        self.distance = distance


def is_in_grid(row: int, col: int, last_row: int, last_col: int) -> bool:
    """Return whether the cell you want to consider is within the grid.

    Example I got this from calls it "is Valid" but I think is valid encompasses so much more.
    """
    return (row >= 0) and (row < last_row) and (col >= 0) and (col < last_col)


def valid_next_cell(current_letter: str, row: int, col: int, the_grid: dict) -> bool:
    """Return true if you can go to the next cell."""
    # fixes for start and End
    if current_letter == "S":
        current_letter_value = 9999999999999999999
    elif current_letter == "E":
        current_letter_value = -9999999999999999999
    else:
        current_letter_value = ord(current_letter)
    next_letter = the_grid[(row, col)]
    if next_letter == "":
        return False
    else:
        next_letter_value = ord(next_letter)
    print(f"{current_letter=} with {current_letter_value=} and {next_letter=} with {next_letter_value=}")
    return next_letter_value <= current_letter_value or next_letter_value == current_letter_value + 1


def breadth_first_search(the_grid, source: Point, destination: Point, last_row: int, last_col: int) -> int:
    print(f"Within bfs {last_row=}, {last_col=}")
    """Find the shortest path from a source cell to a destination cell."""
    row_directions = [-1, 0, 0, 1]
    column_directions = [0, -1, 1, 0]

    # here the example I got this from checks if source and destination have a value of 1 because
    # the example involves only being able to consider points that have a value of 1
    visited = [[False for _ in range(last_col)] for _ in range(last_row)]

    # mark the source cell as visited
    visited[source.x][source.y] = True

    # Create BFS queue
    queue = deque()

    # Distance of source cell is 0
    s = QueueNode(source, 0)
    queue.append(s)

    # BFS starting from source cell
    while queue:
        current = queue.popleft()  # deque from the front cell

        # if we have reached the destination cell, we are done
        point = current.point
        if point.x == destination.x and point.y == destination.y:
            return current.distance

        # we didn't find the final cell, enqueue the adjacent cells
        for i in range(4):
            row = point.x + row_directions[i]
            col = point.y + column_directions[i]

            print(f"checking {row=}, {col=}")
            print(f"Would this row and column be in the grid? {is_in_grid(row, col, last_row, last_col)}")
            # adjacent cell is within bounds, has a path, and is not visited yet so enqueue it
            if is_in_grid(row, col, last_row, last_col) and valid_next_cell(the_grid[(point.x, point.y)],
                                                                            row, col,
                                                                            the_grid) and not visited[row][col]:
                # print("valid!")
                visited[row][col] = True
                print(f"Current letter is at ({point.x},{point.y}) and is {the_grid[(point.x, point.y)]}")
                print(f"Next letter would be at {(row, col)=} and would be {the_grid[(row, col)]}")
                adjacent_cell = QueueNode(Point(row, col), current.distance + 1)
                queue.append(adjacent_cell)
    print("no destination")
    return -1  # couldn't get to the destination


if __name__ == "__main__":
    our_input = input_per_line("../sample_input.txt")
    grid, max_row, max_col = text_to_grid(our_input)
    print(f"{max_row=}")
    print(f"{max_col=}")
    print(grid)
    start, end = find_start_and_end(grid)
    start_point = Point(start[0], start[1])
    end_point = Point(end[0], end[1])
    print(f"{end=}")
    steps_to_end = breadth_first_search(grid, start_point, end_point, max_row, max_col)
    print(f"{steps_to_end=}")
