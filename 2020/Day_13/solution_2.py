def grab_timetable(input_file):
    with open(input_file, 'r') as file:
        raw_timetable = file.readlines()
        bus_lines = raw_timetable[1].split(',')
        bus_lines_with_numbers = []
        for bus in bus_lines:
            try:
                bus_lines_with_numbers.append(int(bus))
            except:
                bus_lines_with_numbers.append(bus)
    return bus_lines_with_numbers


def find_timestamp(timetable):
    number_to_check = 900  # starting high because I know we need to go high
    while True:
        denominator = 0
        all_denominators = set()
        for position, bus in enumerate(timetable):
            if isinstance(bus, int):
                denominator = (number_to_check + position) % bus
                all_denominators.add(denominator)
        if len(all_denominators) == 1:
            return number_to_check
        else:
            number_to_check += 1


def answer_calculation(original_time, bus_id_timestamp):
    wait_time = bus_id_timestamp[1] - original_time
    return bus_id_timestamp[0] * wait_time


if __name__ == "__main__":
    the_timetable = grab_timetable('input')
    earliest_bus_and_id = find_earliest_bus_id_timestamp(the_timetable)
    the_answer = answer_calculation(the_timetable[0], earliest_bus_and_id)
    print(f"The answer is {the_answer}")
