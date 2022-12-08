"""Solution for AoC 2022 Day 07 - No Space Left on Device."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def find_directory_sizes(these_directory: dict, key_to_check: str) -> int:
    """Will return the sum of all file sizes in a directory structure.
    Will 'double count' sub-directories.
    """
    return sum(item if isinstance(item, int) else find_directory_sizes(these_directory, item)
               for item in these_directory[key_to_check])


if __name__ == "__main__":
    history = input_per_line("../input.txt")
    directories: dict = {"/1": []}
    current_directory = []
    depth = 0
    for line in history:
        if current_directory:
            previous_dir = current_directory[-1]
        else:
            previous_dir = ""
        components = line.split()
        if components[0] == "$":
            if components[1] == "cd":
                if components[2] == "..":
                    current_directory.pop()
                    depth -= 1
                else:
                    depth += 1
                    current_directory.append(components[2]+str(depth)+previous_dir)
                    directories[components[2]+str(depth)+previous_dir] = []
        elif components[0] == "dir":
            directories[current_directory[-1]].append(components[1]+str(depth+1)+previous_dir)
        else:  # files
            directories[current_directory[-1]].append(int(components[0]))
    dictionary_of_file_sizes = {directory: find_directory_sizes(directories, directory) for directory in directories}
    large_enough_files = [size for size in dictionary_of_file_sizes.values() if size <= 100000]
    print(f"The total size of the the directories large enough to delete is {sum(large_enough_files)}")
    total_disk_space = 70000000
    space_needed_for_install = 30000000
    current_free_space = total_disk_space - dictionary_of_file_sizes["/1"]
    space_needed_to_clear = space_needed_for_install - current_free_space
    print(f"{current_free_space=}")
    all_directory_sizes = sorted([size for size in dictionary_of_file_sizes.values() if size >= space_needed_to_clear])
    print(f"Smallest directory that can be deleted has a size of {all_directory_sizes[0]}.")

    # 25773269 is too high