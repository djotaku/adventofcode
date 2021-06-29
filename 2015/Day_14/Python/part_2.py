import re
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


class Reindeer:
    def __init__(self, speed, flying_time, resting_time):
        self.speed = speed
        self.flying_time = flying_time
        self.original_flying_time = flying_time
        self.resting_time = resting_time
        self.original_resting_time = resting_time
        self.total_distance = 0
        self.points = 0

    def move(self):
        if self.resting_time == 0:
            self.flying_time = self.original_flying_time
            self.resting_time = self.original_resting_time
        if self.flying_time > 0:
            self.total_distance += self.speed
            self.flying_time -= 1
        elif self.resting_time > 0:
            self.resting_time -= 1

    def __gt__(self, other):
        return self.total_distance > other.total_distance


def figure_out_reindeer_specs(line):
    regex = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    results = re.findall(regex, line)
    reindeer_name, speed, fly_time, rest_time = results[0][0], results[0][1], results[0][2], results[0][3]
    return reindeer_name, int(speed), int(fly_time), int(rest_time)


def create_reindeer_list(attribute_list):
    reindeer_list = []
    for reindeer in attribute_list:
        reindeer_name, speed, fly_time, rest_time = figure_out_reindeer_specs(reindeer)
        reindeer_list.append(Reindeer(speed, fly_time, rest_time))
    return reindeer_list


def move_and_assign_points(list_of_reindeer, total_seconds):
    while total_seconds > 0:
        for reindeer in list_of_reindeer:
            reindeer.move()
        list_of_reindeer = sorted(list_of_reindeer)
        list_of_reindeer[-1].points += 1
        # print("----------")
        for reindeer in list_of_reindeer:
            # print(f"{total_seconds}")
            # print(f"{reindeer.total_distance=}")
            # print(f"{reindeer.points=}")
            pass
        # print("----------")

        total_seconds -= 1


if __name__ == "__main__":
    reindeer_attributes = parse_input.input_per_line('../input.txt')
    all_reindeer = create_reindeer_list(reindeer_attributes)
    move_and_assign_points(all_reindeer, 2503)
    highest_points = 0
    for reindeer in all_reindeer:
        if reindeer.points > highest_points:
            highest_points = reindeer.points
    print(f"The highest-scoring reindeer got {highest_points} points.")


# 1355 is too high
# 1251 is too low
