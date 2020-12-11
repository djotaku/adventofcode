def import_joltages(input_file):
    with open(input_file, 'r') as file:
        return [int(line) for line in file.readlines()]


def check_combinations(list_of_adapters):
    for number, item in enumerate(list_of_adapters):
        if number == 0:
            if list_of_adapters[number] > 3:
                return False
        else:
            if list_of_adapters[number] - list_of_adapters[number-1] > 3:
                return False
    return True


def adapter_combinations(jolt_list, pop_index):
    sorted_jolt_list = sorted(jolt_list)
    combinations = 1  # assume at least one combination works
    while True:
        if not sorted_jolt_list:
            break
        new_sorted_list = sorted_jolt_list.copy()
        new_sorted_list.pop(pop_index)
        if check_combinations(new_sorted_list):
            combinations += 1
            adapter_combinations(new_sorted_list, 0)
        else:
            adapter_combinations(sorted_jolt_list, pop_index+1)
    return combinations


if __name__ == "__main__":
    joltage_list = import_joltages('input')
    combo_number = adapter_combinations(joltage_list, 0)
    print(f"And the answer is {combo_number}")
