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
    for bus in timetable[1]:
        aligned_timestamp = timetable[0]
        if isinstance(bus, int):
            while aligned_timestamp % bus != 0:
                print(timetable[0]%bus)
                aligned_timestamp += 1
            print(f"It lines up at {aligned_timestamp}")
    return None