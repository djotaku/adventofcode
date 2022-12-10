"""Solution to AoC 2022 Day 10 - Cathode-Ray Tube"""


def input_per_line(file: str):
    """This is for when each line is an input to the puzzle. The newline character is stripped."""
    with open(file, 'r') as input_file:
        return [line.rstrip() for line in input_file.readlines()]


def program_execution(assembly: list) -> (list, list):
    """Take in list of assembly code and return list of signal strengths."""
    signal_strengths = []
    register_x = 1
    cycle = 1
    sprite_to_draw = 0
    message = []
    for assembly_code in assembly:
        match assembly_code:
            case "noop":
                cycle += 1
                sprite_to_draw = sprite_location(sprite_to_draw)
                message.append(draw_sprite(sprite_to_draw, register_x))
            case _:
                cycle += 1
                sprite_to_draw = sprite_location(sprite_to_draw)
                message.append(draw_sprite(sprite_to_draw, register_x))
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    signal_strengths.append(register_x * cycle)
                command = assembly_code.split()
                register_x += int(command[1])
                cycle += 1
                sprite_to_draw = sprite_location(sprite_to_draw)
                message.append(draw_sprite(sprite_to_draw, register_x))
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            signal_strengths.append(register_x * cycle)
    return signal_strengths, message


def sprite_location(sprite: int) -> int:
    """Figure out next location for the sprite"""
    sprite += 1
    if sprite % 40 == 0:
        sprite = 0
    return sprite


def draw_sprite(sprite: int, horizontal: int) -> str:
    """Determine whether to draw a . or #"""
    if horizontal == (sprite - 1) or horizontal == sprite or horizontal == (sprite + 1):
        return "#"
    else:
        return "."

if __name__ == "__main__":
    code_to_execute = input_per_line("../input.txt")
    executed_signal_strengths, this_message = program_execution(code_to_execute)
    print(f"{this_message=}")
    print(f"Sum of the signal strengths is {sum(executed_signal_strengths)}")
    print("Message is:")
    print(this_message[0], end="")
    for index, character in enumerate(this_message, start=1):
        if index % 40 == 0:
            print()
            print(character, end="")
        else:
            print(character, end="")
