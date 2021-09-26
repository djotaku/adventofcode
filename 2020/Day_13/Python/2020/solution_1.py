def grab_timetable(input_file):
    with open(input_file, 'r') as file:
        raw_timetable = file.readlines()
        earliest_departure = int(raw_timetable[0].rstrip())
        bus_lines = raw_timetable[1].split(',')
        bus_lines_with_numbers = []
        for bus in bus_lines:
            try:
                bus_lines_with_numbers.append(int(bus))
            except:
                bus_lines_with_numbers.append(bus)
    return earliest_departure, bus_lines_with_numbers


def find_earliest_bus_id_timestamp(timetable):
    bus_id_timestamp = []
    for bus in timetable[1]:
        aligned_timestamp = timetable[0]
        if isinstance(bus, int):
            while aligned_timestamp % bus != 0:
                aligned_timestamp += 1
            bus_id_timestamp.append((bus, aligned_timestamp))
    bus_to_grab = bus_id_timestamp[0]
    for return_items in bus_id_timestamp:
        if return_items[1] < bus_to_grab[1]:
            bus_to_grab = return_items
    return bus_to_grab


def answer_calculation(original_time, bus_id_timestamp):
    wait_time = bus_id_timestamp[1] - original_time
    return bus_id_timestamp[0] * wait_time


if __name__ == "__main__":
    the_timetable = grab_timetable('input')
    earliest_bus_and_id = find_earliest_bus_id_timestamp(the_timetable)
    the_answer = answer_calculation(the_timetable[0], earliest_bus_and_id)
    print(f"The answer is {the_answer}")
