"""Solution for AoC 2022 Day 07 - No Space Left on Device."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_directory_sizes(these_directory: dict, key_to_check: str) -> int:
    """Will return the sum of all file sizes in a directory structure.
    Will 'double count' sub-directories.
    """
    file_sizes = 0
    for item in these_directory[key_to_check]:
        if isinstance(item, int):
            file_sizes += item
        else:
            file_sizes += find_directory_sizes(these_directory, item)
    return file_sizes


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
    dictionary_of_file_sizes = {directory: find_directory_sizes(directories, directory) for directory in directories}
    large_enough_files = [size for size in dictionary_of_file_sizes.values() if size <= 100000]
    print(f"The total size of the the directories large enough to delete is {sum(large_enough_files)}")

# 73314807 is too high