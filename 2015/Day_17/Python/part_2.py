from sys import path
from itertools import combinations
path.insert(0, '../../input_parsing')
import parse_input

container_sizes = parse_input.input_per_line('../input.txt')
container_sizes = [int(x) for x in container_sizes]
all_ways = [element for size in range(1, len(container_sizes))
            for element in combinations(container_sizes, size) if sum(element) == 150]
minimum_number_of_containers = 999999999999
for combination in all_ways:
    if len(combination) < minimum_number_of_containers:
        minimum_number_of_containers = len(combination)
all_ways = [combination for combination in all_ways if len(combination) == minimum_number_of_containers]
print(f"The number of combinations for using my containers is {len(all_ways)}")
