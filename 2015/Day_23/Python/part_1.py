from sys import path
path.insert(0, '../../input_parsing')
import parse_input


if __name__ == "__main__":
    assembly = parse_input.input_per_line('../input.txt')
    pointer = 0
    register_a = 0
    register_b = 0
    while pointer < len(assembly):
        current_instruction = assembly[pointer].split()
        if len(current_instruction) == 2:
            if current_instruction[0] == "hlf":
                if current_instruction[1] == "a":
                    register_a = register_a / 2
                else:
                    register_b = register_b / 2
                pointer += 1
            elif current_instruction[0] == "tpl":
                if current_instruction[1] == "a":
                    register_a *= 3
                else:
                    register_b *= 3
                pointer += 1
            elif current_instruction[0] == "inc":
                if current_instruction[1] == "a":
                    register_a += 1
                else:
                    register_b += 1
                pointer += 1
            elif current_instruction[0] == "jmp":
                pointer += int(current_instruction[1])
        elif len(current_instruction) == 3:
            if current_instruction[0] == "jie":
                if current_instruction[1].strip(',') == "a":
                    if register_a % 2 == 0:
                        pointer += int(current_instruction[2])
                    else:
                        pointer += 1
                else:
                    if register_b % 2 == 0:
                        pointer += int(current_instruction[2])
                    else:
                        pointer += 1
            elif current_instruction[0] == "jio":
                if current_instruction[1].strip(',') == "a":
                    if register_a == 1:
                        pointer += int(current_instruction[2])
                    else:
                        pointer += 1
                else:
                    if register_b == 1:
                        pointer += int(current_instruction[2])
                    else:
                        pointer += 1
    print(f"When it's all done, the value in {register_b=}")
