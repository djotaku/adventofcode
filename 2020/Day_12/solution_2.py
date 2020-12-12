import math

def parse_input(file_input):
    with open(file_input, 'r') as file:
        return [(row[0], int(row[1:].rstrip())) for row in file.readlines()]


def orientation(directions, east_west, north_south):
    degrees = directions[1]
    new_east_west = 0
    new_north_south = 0
    if directions[0] == 'R':
        new_east_west = math.cos(math.radians(degrees)) * east_west + math.sin(math.radians(degrees)) * north_south
        new_north_south = -math.sin(math.radians(degrees)) * east_west + math.cos(math.radians(degrees)) * north_south
    elif directions[0] == 'L':
        new_east_west = math.cos(math.radians(-degrees)) * east_west + math.sin(math.radians(-degrees)) * north_south
        new_north_south = math.sin(math.radians(-degrees)) * east_west + math.cos(math.radians(-degrees)) * north_south
    print(f'{degrees=}')
    print(f'{new_east_west=}, {new_north_south=}')
    return round(new_east_west), round(new_north_south)


def move_boat(directions):
    boat_north_south = 0
    boat_east_west = 0
    waypoint_north_south = 1
    waypoint_east_west = 10
    for direction in directions:
        print(f'{boat_north_south=}')
        print(f'{boat_east_west=}')
        print(f'{waypoint_north_south=}')
        print(f'{waypoint_east_west=}')
        print('------------------')
        if direction[0] == 'F':
            east_west_movement = direction[1] * waypoint_east_west
            north_south_movement = direction[1] * waypoint_north_south
            boat_east_west += east_west_movement
            boat_north_south += north_south_movement
        elif direction[0] == 'L' or direction[0] == 'R':
            waypoint_east_west, waypoint_north_south = orientation(direction, waypoint_east_west, waypoint_north_south)
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

#8699 is too low
#7270 is too low