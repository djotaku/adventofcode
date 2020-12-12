def parse_input(file_input):
    with open(file_input, 'r') as file:
        return [(row[0], int(row[1:].rstrip())) for row in file.readlines()]


def orientation(directions, current_orientation):
    cardinal_directions = ['north', 'east', 'south', 'west']
    position_in_directions = cardinal_directions.index(current_orientation)
    degrees = directions[1]
    while degrees !=0:
        if directions[0] == 'R':
            position_in_directions += 1
            if position_in_directions == len(cardinal_directions):
                position_in_directions = 0
            degrees -= 90
        elif directions[0] == 'L':
            position_in_directions -= 1
            if position_in_directions < 0:
                position_in_directions = len(cardinal_directions) - 1
            degrees -= 90
    return cardinal_directions[position_in_directions]


def move_boat(directions):
    north_south = 0
    east_west = 0
    boat_orientation = 'east'
    for direction in directions:
        print(f'{north_south}')
        print(f'{east_west}')
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
            boat_orientation = orientation(direction, boat_orientation)
        elif direction[0] == 'N':
            north_south += direction[1]
        elif direction[0] == 'S':
            north_south -= direction[1]
        elif direction[0] == 'E':
            north_south += direction[1]
        elif direction[0] == 'W':
            north_south -= direction[1]
    return abs(north_south) + abs(east_west)


if __name__ == "__main__":
    print(move_boat(parse_input('input')))

# 1593 is too high