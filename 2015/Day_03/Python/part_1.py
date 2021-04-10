import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def separate_directions(direction):
    """Take the long text line of directions and split into discrete directions."""
    return [char for char in direction]


def count_houses_visited(directions):
    """Take a list of directions and create coordinates."""
    coordinates = {(0, 0)}
    coordinate = [0, 0]
    for direction in directions:
        if direction == "^":
            coordinate[1] += 1
            coordinates.add((coordinate[0], coordinate[1]))
        elif direction == "v":
            coordinate[1] -= 1
            coordinates.add((coordinate[0], coordinate[1]))
        elif direction == "<":
            coordinate[0] -= 1
            coordinates.add((coordinate[0], coordinate[1]))
        elif direction == ">":
            coordinate[0] += 1
            coordinates.add((coordinate[0], coordinate[1]))
    return len(coordinates)


if __name__ == "__main__":
    santa_directions = parse_input.input_per_line('../input.txt')
    print(f"{count_houses_visited(separate_directions(santa_directions[0]))} houses received at least one present "
          f"from Santa")
