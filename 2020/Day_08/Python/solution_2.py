def instruction_parsing(instruction):
    return instruction.rstrip().split()


def evaluate_command(command):
    if command[0] == 'nop':
        return 1, 0
    elif command[0] == 'acc':
        return 1, int(command[1])
    elif command[0] == 'jmp':
        return int(command[1]), 0


def change_command(command):
    if command[0] == 'jmp':
        return ['nop', command[1]]
    elif command[0] == 'nop':
        return ['jmp', command[1]]
    else:
        return command


def assembly_runner(instructions):
    accumulator = 0
    position_tracker = []
    position = 0
    # First time through
    position_tracker.append(position)
    position_delta, accumulator_delta = evaluate_command(instructions[position])
    position += position_delta
    accumulator += accumulator_delta
    while True:
        if position == len(instructions):
            print("We reached the end")
            return False, accumulator
        if position in position_tracker:
            print("Danger of Infinite Loop!")
            return True, accumulator
        else:
            position_tracker.append(position)
            position_delta, accumulator_delta = evaluate_command(instructions[position])
            position += position_delta
            accumulator += accumulator_delta


def alter_me(instructions, counter):
    instructions[counter] = change_command(instructions[counter])
    return instructions


if __name__ == "__main__":
    with open('input', 'r') as file:
        instructions = [instruction_parsing(instruction) for instruction in file.readlines()]
        final_accumulation = 0
        counter = 0
        brute_force = True
        while brute_force:
            brute_force, final_accumulation = assembly_runner(instructions)
            if brute_force:
                instructions = alter_me(instructions, counter)
                brute_force, final_accumulation = assembly_runner(instructions)
                instructions = alter_me(instructions, counter)
                counter += 1
    print(f'Final {final_accumulation=}')
