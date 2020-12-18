def parse_input(input_file):
    with open(input_file, 'r') as file:
        return [[char for char in line if char != ' '] for line in file.readlines()]


def new_math(math_stack):
    final_sum = 0
    left_number = 0
    operator = ''
    parenthesis = False
    parenthesis_count = 0
    parenthesis_list = []
    for item in math_stack:
        if item.isdigit() and not parenthesis:
            if left_number == 0:
                left_number = item
            else:
                print(f'{item=}')
                print(f'{left_number}{operator}{item}')
                final_sum = eval(f'{left_number}{operator}{item}')
                left_number = final_sum
        elif parenthesis:
            if item != ')' and parenthesis_count == 1:
                parenthesis_list.append(item)
            elif item == ')' and parenthesis_count == 1:
                paren_sum = new_math(parenthesis_list.copy())
                parenthesis_count = 0
                parenthesis_list.clear()
                final_sum = eval(f'{left_number}{operator}{paren_sum}')
                left_number = final_sum
        elif item == "(":
            parenthesis = True
            parenthesis_count += 1
        elif item == ')':
            parenthesis = False
        else:
            operator = item
        print('--------')
        print(f'{final_sum=}')
        print(f'{operator=}')
        print('--------------')
    return final_sum