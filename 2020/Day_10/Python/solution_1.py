def import_joltages(input_file):
    with open(input_file, 'r') as file:
        return [int(line) for line in file.readlines()]


def jolt_differences(jolt_list):
    sorted_jolt_list = sorted(jolt_list)
    jolt = 0
    one_jolt_counter = 0
    three_jolt_counter = 0
    for adapter in sorted_jolt_list:
        jolt_difference = adapter - jolt
        if jolt_difference == 1:
            one_jolt_counter += 1
        elif jolt_difference == 3:
            three_jolt_counter += 1
        jolt = adapter
    three_jolt_counter += 1  # for your final adapter
    return one_jolt_counter, three_jolt_counter


if __name__ == "__main__":
    jolts_to_multiply = jolt_differences(import_joltages('input'))
    answer = jolts_to_multiply[0] * jolts_to_multiply[1]
    print(f"And the answer is {answer}")