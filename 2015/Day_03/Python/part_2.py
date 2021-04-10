import sys
sys.path.insert(0, '../../input_parsing')
import parse_input


def separate_directions(direction):
    """Take the long text line of directions and split into discrete directions."""
    return [char for char in direction]


def count_houses_visited(directions):
    """Take a list of directions and create coordinates."""
    coordinates = {(0, 0)}
    santa_coordinate = [0, 0]
    robo_santa_coordinate = [0,0]
    for count, direction in enumerate(directions):
        if direction == "^":
            if count == 0 or count % 2 == 0:
                santa_coordinate[1] += 1
                coordinates.add((santa_coordinate[0], santa_coordinate[1]))
            else:
                robo_santa_coordinate[1] += 1
                coordinates.add((robo_santa_coordinate[0], robo_santa_coordinate[1]))
        elif direction == "v":
            if count == 0 or count % 2 == 0:
                santa_coordinate[1] -= 1
                coordinates.add((santa_coordinate[0], santa_coordinate[1]))
            else:
                robo_santa_coordinate[1] -= 1
                coordinates.add((robo_santa_coordinate[0], robo_santa_coordinate[1]))
        elif direction == "<":
            if count == 0 or count % 2 == 0:
                santa_coordinate[0] -= 1
                coordinates.add((santa_coordinate[0], santa_coordinate[1]))
            else:
                robo_santa_coordinate[0] -= 1
                coordinates.add((robo_santa_coordinate[0], robo_santa_coordinate[1]))
        elif direction == ">":
            if count == 0 or count % 2 == 0:
                santa_coordinate[0] += 1
                coordinates.add((santa_coordinate[0], santa_coordinate[1]))
            else:
                robo_santa_coordinate[0] += 1
                coordinates.add((robo_santa_coordinate[0], robo_santa_coordinate[1]))
    return len(coordinates)


if __name__ == "__main__":
    santa_directions = parse_input.input_per_line('../input.txt')
    print(f"{count_houses_visited(separate_directions(santa_directions[0]))} houses received at least one present "
          f"from Santa or Robo-Santa")
