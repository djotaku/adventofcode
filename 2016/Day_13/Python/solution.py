"""Solution to AoC 2016 Day 13 - A Maze of Twisty Little Cubicles."""
from collections import  deque


def binary_representation(number: int) -> list:
    """Return binary representation of a number as a list of 1s or 0s."""
    binary_number = []
    while number > 0:
        binary_number.append(number%2)
        number = number // 2
    binary_number.reverse()
    return binary_number

def wall_or_space(x: int, y: int, favorite_number: int) -> bool:
    """Return true if open space and false if it's a wall."""
    equation = x*x + 3*x + 2*x*y + y + y*y
    value = equation + favorite_number
    binary_value = binary_representation(value)
    if sum(binary_value) % 2 == 0:
        return True
    else:
        return False


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x}, {self.y})"


class QueueNode:
    """A data structure for queue used in BFS"""

    def __init__(self, point: Point, distance: int):
        self.point = point
        self.distance = distance

# no grid in this version since it's defined on the fly based on coordinates.
def breadth_first_search(source: Point, destination: Point, last_row: int, last_col: int, fav_num: int) -> int:
    # print(f"Within bfs {last_row=}, {last_col=}")
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
            x = point.x + row_directions[i]
            y = point.y + column_directions[i]

            # print(f"checking {row=}, {col=}")
            # print(f"Would this row and column be in the grid? {is_in_grid(row, col, last_row, last_col)}")
            # adjacent cell is within bounds, has a path, and is not visited yet so enqueue it
            if wall_or_space(x, y, fav_num) and x > 0 and y > 0 and not visited[x][y]:
                # print("valid!")
                visited[x][y] = True
                # print(f"Current letter is at ({point.x},{point.y}) and is {the_grid[(point.x, point.y)]}")
                # print(f"Next coordinates could be at {(x, y)=} ")
                adjacent_cell = QueueNode(Point(x, y), current.distance + 1)
                queue.append(adjacent_cell)
    # print("no destination")
    return -1  # couldn't get to the destination

if __name__ == "__main__":
    debug = False
    if debug:
        lucky_number = 10
        end_point = Point(7, 4)
    else:
        lucky_number = 1350
        end_point = Point(31, 39)
    starting_point = Point(1,1)
    number_of_steps = breadth_first_search(starting_point, end_point, 999, 999, lucky_number)
    print(f"Number of steps to go from {starting_point} to {end_point} is {number_of_steps}.")