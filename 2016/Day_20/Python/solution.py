"""Solution to AoC 2016 Day 2016: Firewall Rules."""
import re


def range_to_list(range_string: str) -> list:
    regex = re.compile(r'([0-9]+)\-([0-9]+)')
    numbers = re.findall(regex, range_string)
    minimum = numbers[0][0]
    maximum = numbers[0][1]
    return [number for number in range(int(minimum), int(maximum) + 1)]


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


if __name__ == "__main__":
    MAX_IP = 9
    all_potential_ips = [number for number in range(0, MAX_IP + 1)]
    all_potential_ips_set = set(all_potential_ips)
    banned_ip_range_list = input_per_line('test_input.txt')
    banned_ips_set = set()
    for ips in banned_ip_range_list:
        ip_list = range_to_list(ips)
        for ip in ip_list:
            banned_ips_set.add(ip)
    valid_ips = all_potential_ips_set - banned_ips_set
    print(f"The lowest non-blocked IP is:{min(valid_ips)}")
