from itertools import combinations, permutations
from math import prod
from statistics import mean
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


if __name__ == "__main__":
    packages = parse_input.input_per_line('../input.txt')
    packages = [int(x) for x in packages]
    # test
    # packages = [1,2,3,4,5,7,8,9,10,11]
    weight_per_section = sum(packages) / 3
    print(f"{weight_per_section=}")
    package_combinations = [element for size in range(1, len(packages))
                            for element in combinations(packages, size)
                            if sum(element) == weight_per_section]
    # print(package_combinations)
    # figure out smallest group 1 size
    santa_leg_room_packages = 100000000000000000
    for combination in package_combinations:
        if len(combination) < santa_leg_room_packages:
            santa_leg_room_packages = len(combination)
    group_1_contenders = [combination for combination in package_combinations
                          if len(combination) == santa_leg_room_packages]
    print(group_1_contenders)
    if len(group_1_contenders) == 1:
        print(f"The quantum entanglement of the packages in Santa's leg area is: {prod(group_1_contenders[0])}.")
    else:
        quantum_entanglement = 10000000000000000000000
        for presents in group_1_contenders:
            if prod(presents) < quantum_entanglement:
                quantum_entanglement = prod(presents)
        print(f"The quantum entanglement of the packages in Santa's leg area is: {quantum_entanglement}.")