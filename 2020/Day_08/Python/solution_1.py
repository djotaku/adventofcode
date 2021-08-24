def instruction_parsing(instruction):
    return instruction.rstrip().split()


def evaluate_command(command):
    if command[0] == 'nop':
        return 1, 0
    elif command[0] == 'acc':
        return 1, int(command[1])
    elif command[0] == 'jmp':
        return int(command[1]), 0


if __name__ == "__main__":
    with open('input', 'r') as file:
        instructions = [instruction_parsing(instruction) for instruction in file.readlines()]
        accumulator = 0
        position_tracker = []
        position = 0
        # First time through
        position_tracker.append(position)
        position_delta, accumulator_delta = evaluate_command(instructions[position])
        position += position_delta
        accumulator += accumulator_delta
        while True:
            if position in position_tracker:
                print("Danger of Infinite Loop!")
                print(f'{accumulator=}')
                break
            else:
                position_tracker.append(position)
                position_delta, accumulator_delta = evaluate_command(instructions[position])
                position += position_delta
                accumulator += accumulator_delta
