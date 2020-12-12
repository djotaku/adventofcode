import math

def parse_input(file_input):
    with open(file_input, 'r') as file:
        return [(row[0], int(row[1:].rstrip())) for row in file.readlines()]


def orientation(directions, east_west, north_south):
    degrees = directions[1]
    if directions[0] == 'R':
        new_east_west = math.cos(math.radians(degrees)) * east_west + math.sin(math.radians(degrees)) * north_south
        new_north_south = -math.sin(math.radians(degrees)) * east_west + math.cos(math.radians(degrees)) * north_south
    elif directions[0] == 'L':
        new_east_west = math.cos(math.radians(-degrees)) * east_west + math.sin(math.radians(-degrees)) * north_south
        new_north_south = math.sin(math.radians(-degrees)) * east_west + math.cos(math.radians(-degrees)) * north_south
    return int(new_east_west), int(new_north_south)


def move_boat(directions):
    boat_north_south = 0
    boat_east_west = 0
    waypoint_north_south = 1
    waypoint_east_west = 10
    boat_orientation = 'east'
    for direction in directions:
        print(f'{north_south}')
        print(f'{east_west}')
        print(f'{boat_orientation}')
        print('------------------')
        if direction[0] == 'F':
            if boat_orientation == 'east':
                east_west += direction[1]
            elif boat_orientation == 'west':
                east_west -= direction[1]
            elif boat_orientation == 'north':
                north_south += direction[1]
            elif boat_orientation == 'south':
                north_south -= direction[1]
        elif direction[0] == 'L' or direction[0] == 'R':
            boat_orientation = orientation(direction, waypoint_east_west, waypoint_north_south)
        elif direction[0] == 'N':
            waypoint_north_south += direction[1]
        elif direction[0] == 'S':
            waypoint_north_south -= direction[1]
        elif direction[0] == 'E':
            waypoint_east_west += direction[1]
        elif direction[0] == 'W':
            waypoint_east_west -= direction[1]
    return abs(boat_north_south) + abs(boat_east_west)


if __name__ == "__main__":
    print(move_boat(parse_input('input')))

