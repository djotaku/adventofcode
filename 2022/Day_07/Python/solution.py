"""Solution for AoC 2022 Day 07 - No Space Left on Device."""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


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
            elif components[1] == "ls":
                pass  # don't need to do anything because the rest of lines until we get to "$" is a listing
        elif components[0] == "dir":
            directories[current_directory[-1]].append({components[1]: []})
        else:  # files
            directories[current_directory[-1]].append({components[1]: int(components[0])})
    print(directories)