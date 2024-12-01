from collections import Counter
def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

if __name__ == '__main__':
    locations = input_per_line("../input.txt")
    left_side = []
    right_side = []
    for line in locations:
        entries = line.split()
        left_side.append(int(entries[0]))
        right_side.append(int(entries[1]))
    left_side.sort()
    right_side.sort()
    distances = [abs(right_side[number]-left_item) for number, left_item in enumerate(left_side)]
    print(f"The total distance between the lists is {sum(distances)}")
    right_side_count = Counter(right_side)
    similarity_list = [item * right_side_count[item] for item in left_side]
    print(f"The similarity score is {sum(similarity_list)}")
