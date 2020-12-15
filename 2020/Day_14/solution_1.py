import re


def get_mem(a_mem_line):
    return re.findall(r'\d+', a_mem_line)


def parse_input(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        all_instruction = []
        mask_and_instructions = []
        for line in lines:
            test = line.split('=')
            if test[0] == "mask " and not mask_and_instructions:
                mask_and_instructions = [(test[1].rstrip()).lstrip()]
            if test[0] == "mask ":
                all_instruction.append(mask_and_instructions.copy())
                mask_and_instructions.clear()
                mask_and_instructions = [(test[1].rstrip()).lstrip()]
            else:
                instruction = get_mem(line)
                mask_and_instructions.append((int(instruction[0]), int(instruction[1])))
        if not all_instruction:
            all_instruction.append(mask_and_instructions)
    return all_instruction


def mask_application(mask, initial_number):
    binary = (str(bin(initial_number))).lstrip('0b')
    how_many_zeroes = 36-len(binary)
    value = "0"*how_many_zeroes + binary
    mask_as_list = [char for char in mask]
    value_as_list = [char for char in value]
    for position, mask_bit in enumerate(mask_as_list):
        # print(f'{mask_bit=}')
        if mask_bit == '1':
            # print(f"There is a 1 at {position=}")
            new_value = int(value_as_list[position], 2) | 1
            value_as_list[position] = str(new_value)
        elif mask_bit == '0':
            new_value = int(value_as_list[position], 2) & 0
            value_as_list[position] = str(new_value)
    back_to_number = ''.join(value_as_list)
    return int(back_to_number, 2)


if __name__ == "__main__":
    the_input = parse_input('input')
    output_list = [0 for number in range(0, 100000)]
    for instruction in the_input:
        for index in range(1, len(instruction)-1):
            answer = mask_application(instruction[0], instruction[index][1])
            output_list[instruction[index][0]] = answer
    print(sum(output_list))

#11960996660804 is too low