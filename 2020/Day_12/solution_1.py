def parse_input(file_input):
    with open(file_input, 'r') as file:
        return [(row[0], int(row[1:].rstrip())) for row in file.readlines()]