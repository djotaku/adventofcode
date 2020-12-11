from collections import Counter

def import_joltages(input_file):
    with open(input_file, 'r') as file:
        return [int(line) for line in file.readlines()]


if __name__ == "__main__":
    joltage_list = sorted(import_joltages('input') + [0])
    print(joltage_list)
    c = Counter({0: 1})
    for adapter in joltage_list:
        c[adapter + 1] += c[adapter]
        c[adapter + 2] += c[adapter]
        c[adapter + 3] += c[adapter]

    print(f"And the answer is {c[max(joltage_list)+3]}")
