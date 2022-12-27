"""Solution to AoC 2017 Day 07 - Memory Reallocation."""

def input_only_one_line(file: str):
    """Puzzle input is just one line."""
    with open(file, 'r') as input_file:
        return input_file.readline()

def redistribute_blocks(blocks: list) -> list:
    """Find the highest block and redistribute the contents."""
    max_bank = max(blocks)
    max_bank_index = blocks.index(max_bank)
    blocks[max_bank_index] = 0
    while max_bank > 0:
        max_bank_index += 1
        max_bank_index = max_bank_index % len(blocks)
        blocks[max_bank_index] += 1
        max_bank -= 1
    return blocks

if __name__ == "__main__":
    debug = True
    if debug:
        input_file = "../sample_input.txt"
    else:
        input_file = "../input.txt"
    our_input = input_only_one_line(input_file)
    the_blocks = our_input.split()
    the_blocks = [int(number) for number in the_blocks]
    blocks_string = ""
    for number in the_blocks:
        blocks_string += str(number)
    blocks_seen = {blocks_string}
    cycles = 0
    while True:
        cycles += 1
        the_blocks = redistribute_blocks(the_blocks)
        blocks_string = ""
        for number in the_blocks:
            blocks_string += str(number)
        if blocks_string in blocks_seen:
            break
        else:
            blocks_seen.add(blocks_string)
    print(f"It took {cycles} cycles.")