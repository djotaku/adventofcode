"""Solution for AoC 2022 Day 07 - No Space Left on Device."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]

def find_directory_sizes(these_directory: dict) -> dict:
    """Will return the sum of all file sizes in a directory structure.
    Will 'double count' sub-directories.
    """
    output_dictionary = {}
    for directory in these_directory.keys():
        file_sizes = 0
        for item in directory:
            if isinstance(item, int):
                file_sizes += item
            else:
                file_sizes += find_directory_sizes(item)
        output_dictionary[directory] = file_sizes
    return output_dictionary

if __name__ == "__main__":
    history = input_per_line("../sample_input.txt")
    directories: dict = {"/": []}
    current_directory = []
    for line in history:
        components = line.split()
        if components[0] == "$":
            if components[1] == "cd":
                if components[2] == "..":
                    current_directory.pop()
                else:
                    current_directory.append(components[2])
                    directories[components[2]] = []
        elif components[0] == "dir":
            directories[current_directory[-1]].append(components[1])
        else:  # files
            directories[current_directory[-1]].append(int(components[0]))
    # debug
    print(directories)
    directory_sums = find_directory_sizes(directories)