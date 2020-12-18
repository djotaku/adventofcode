def parse_input(input_file):
    with open(input_file, 'r') as file:
        return [line.split() for line in file.readlines()]


def new_math(math_stack):
    final_sum = 0
    left_number = 0
    operator = ''
    for item in math_stack:
        if item.isdigit():
            if left_number == 0:
                left_number = item
            else:
                print(f'{item=}')
                print(f'{left_number}{operator}{item}')
                final_sum = eval(f'{left_number}{operator}{item}')
                left_number = final_sum
        elif item == "(":
            pass
        elif item == ')':
            pass
        else:
            operator = item
        print('--------')
        print(f'{final_sum=}')
        print(f'{operator=}')
        print('--------------')
    return final_sum