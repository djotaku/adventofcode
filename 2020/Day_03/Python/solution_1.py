with open("input", 'r') as file:
    first_line = file.readline()  # throwaway first row
    rest_of_map = file.readlines()

index = 3
count = 0
for line in rest_of_map:
    print(line)
    if line[index] == "#":
        count = count + 1
        print(f"I am at {index=} and I would have hit a tree")
    index = index + 3
    if index > len(line) - 2:
        index = index - len(line) + 1

print(f'{count=}')