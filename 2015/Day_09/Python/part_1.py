"""Attempt a Hamilton Walk-based solution."""

import re
from collections import defaultdict


def hamilton_walk(graph, starting_point):
    """Expects a graph that is a dictionary where the key is a city and value is a list of connected cities."""
    size = len(graph)
    cities_to_visit = [None, starting_point]   # the none is here to end the upcoming while loop
    path = []
    while cities_to_visit:
        current_city = cities_to_visit.pop()
        if current_city:
            path.append(current_city)
            if len(path) == size:
                break
        for remaining_city in set(graph[current_city]) - set(path):
            cities_to_visit.append(None)
            cities_to_visit.append(remaining_city)
        else:
            pass  # I think this breaks on circular routes?
            #path.pop()
    return path


def all_visits(graph, starting_point):
    """Expects a graph that is a dictionary where the key is a city and value is a list of connected cities."""
    all_cities = set(graph)
    paths = []





def parse_connections(lines):
    regex = re.compile(r'(\w+) to (\w+) = (\d+)')
    hamilton_dict = defaultdict(list)
    for line in lines:
        destinations = re.findall(regex, line)
        value = {destinations[0][1]: destinations[0][2]}
        if destinations[0][0] not in hamilton_dict:
            hamilton_dict[destinations[0][0]] = [value]
        else:
            hamilton_dict[destinations[0][0]].append(value)
    return hamilton_dict


if __name__ == "__main__":
    flight_connections = {"London": ["Dublin", "Belfast"], "Dublin": ["Belfast", "London"],
                          "Belfast": ["London", "Dublin"]}
    #print(hamilton_walk(flight_connections, "London"))
    print(all_visits(flight_connections, "London"))