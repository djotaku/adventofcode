import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def reindeer_distance(speed, flying_time, resting_time, total_time):
    remaining_time = total_time
    flown_distance = 0
    while remaining_time > 0:
        if remaining_time >= flying_time:
            flown_distance += speed * flying_time
            remaining_time -= flying_time
        else:
            flown_distance += speed * remaining_time
            remaining_time = 0
        if remaining_time >= resting_time:
            remaining_time -= resting_time
        else:
            remaining_time = 0
    return flown_distance


def figure_out_reindeer_specs(line):
    regex = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    results = re.findall(regex, line)
    reindeer_name, speed, fly_time, rest_time = results[0][0], results[0][1], results[0][2], results[0][3]
    return reindeer_name, int(speed), int(fly_time), int(rest_time)


if __name__ == "__main__":
    reindeer_list = parse_input.input_per_line('../input.txt')
    top_distance = 0
    for reindeer in reindeer_list:
        reindeer_name, speed, fly_time, rest_time = figure_out_reindeer_specs(reindeer)
        distance_flown = reindeer_distance(speed, fly_time, rest_time, 2503)
        if distance_flown > top_distance:
            top_distance = distance_flown
    print(f"The top-flying reindeer flew {top_distance} km.")
