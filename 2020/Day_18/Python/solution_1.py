def evaluate_parenthesis(equation):
    if '(' not in equation:
        return equation
    else:
        parenthesis_count = 0
        equation_with_parenthesis = []
        parenthesis_left_index = []
        for index in range(0, len(equation)):
            if equation[index] == "(":
                parenthesis_count += 1
                parenthesis_left_index.append(index)
            if equation[index] == ")":
                parenthesis_count -= 1
                if parenthesis_count == 0:
                    equation_with_parenthesis.append(evaluate_parenthesis(equation[parenthesis_left_index[0]+1:index]))
                    parenthesis_left_index.clear()
            if parenthesis_count == 0 and equation[index] != '(' and equation[index] != ")":
                equation_with_parenthesis.append(equation[index])
        return equation_with_parenthesis


def parse_input(input_file):
    with open(input_file, 'r') as file:
        equations = [[char for char in line if char != ' '] for line in file.readlines()]
        fixed_equations = [evaluate_parenthesis(equation) for equation in equations]
        return fixed_equations


def new_math(math_stack):
    final_sum = 0
    left_number = 0
    operator = ''
    for item in math_stack:
        if isinstance(item, list):
            if left_number == 0:
                left_number = new_math(item)
            else:
                paren_sum = new_math(item)
                print(f'{left_number}{operator}{paren_sum}')
                final_sum = eval(f'{left_number}{operator}{paren_sum}')
                left_number = final_sum
        elif item.isdigit():
            if left_number == 0:
                left_number = item
            else:
                #print(f'{item=}')
                print(f'{left_number}{operator}{item}')
                final_sum = eval(f'{left_number}{operator}{item}')
                left_number = final_sum
        else:
            operator = item
        #print('--------')
        #print(f'{final_sum=}')
        #print(f'{operator=}')
        #print('--------------')
    return final_sum


if __name__ == "__main__":
    my_equations = parse_input('input')
    answers = [new_math(equation) for equation in my_equations]
    print(f"The answer is {sum(answers)}")
