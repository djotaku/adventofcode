import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def reindeer_distance(speed, flying_time, resting_time, total_time):
    remaining_time = total_time
    flown_distance = 0
    distance_over_time = []
    original_flying_time = flying_time
    original_resting_time = resting_time
    while remaining_time > 0:
        if flying_time > 0:
            flown_distance += speed
            remaining_time -= 1
            flying_time -= 1
            distance_over_time.append(flown_distance)
        elif resting_time > 0:
            resting_time -= 1
            remaining_time -= 1
            distance_over_time.append(flown_distance)
        else:
            flying_time = original_flying_time
            resting_time = original_resting_time
    return distance_over_time


def figure_out_reindeer_specs(line):
    regex = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    results = re.findall(regex, line)
    reindeer_name, speed, fly_time, rest_time = results[0][0], results[0][1], results[0][2], results[0][3]
    return reindeer_name, int(speed), int(fly_time), int(rest_time)


if __name__ == "__main__":
    reindeer_list = parse_input.input_per_line('../input.txt')
    top_score = 0
    reindeer_dictionary = {}
    for reindeer in reindeer_list:
        reindeer_name, speed, fly_time, rest_time = figure_out_reindeer_specs(reindeer)
        distance_flown = reindeer_distance(speed, fly_time, rest_time, 2503)
        reindeer_dictionary[reindeer_name] = {"distance": distance_flown, "score": 0}
    print(reindeer_dictionary.keys())
    print(f"The top-flying reindeer flew {top_score} km.")
