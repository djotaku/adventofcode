def calculate_slopes(right, down):
    with open("input", 'r') as file:
        file.readline()  # throwaway first row
        if down == 2:
            file.readline()  # throwaway second line
        rest_of_map = file.readlines()
    index = right
    count = 0
    for_cycles = 1
    for line in rest_of_map:
        if down == 2 and for_cycles % 2 == 0:
            for_cycles = for_cycles + 1
            continue
        if line[index] == "#":
            count = count + 1
        index = index + right
        if index > len(line) - 2:
            index = index - len(line) + 1
        for_cycles = for_cycles + 1
    return count


print(calculate_slopes(1, 1))
print(calculate_slopes(3, 1))
print(calculate_slopes(5, 1))
print(calculate_slopes(7, 1))
print(calculate_slopes(1, 2))

print(calculate_slopes(1, 1) * calculate_slopes(3, 1) * calculate_slopes(5, 1) * calculate_slopes(7, 1) *
      calculate_slopes(1, 2))
