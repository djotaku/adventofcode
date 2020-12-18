def evaluate_parenthesis(equation):
    if '(' not in equation:
        return equation
    else:
        parenthesis_count = 0
        equation_with_parenthesis = []
        parenthesis_left_index = []
        for index in range(0, len(equation)):
            print(equation[index])
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
    parenthesis = False
    parenthesis_count = 0
    parenthesis_list = []
    print(f'{parenthesis}')
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
            if item != ')' and parenthesis_count >= 1:
                if item == '(':
                    parenthesis_count += 1
                parenthesis_list.append(item)
                print(f'{parenthesis_list=}')
            elif item == ')' and parenthesis_count >= 1:
                print("end of parenthesis")
                paren_sum = new_math(parenthesis_list.copy())
                print(f'{paren_sum=}')
                print(f'{left_number=}')
                print(f'{operator=}')
                parenthesis_count -= 1
                parenthesis_list.clear()
                parenthesis = False
                final_sum = eval(f'{left_number}{operator}{paren_sum}')
                left_number = final_sum
        elif item == "(":
            parenthesis = True
            parenthesis_count += 1
        #elif item == ')':
        #    parenthesis = False
        else:
            operator = item
        #print('--------')
        #print(f'{final_sum=}')
        #print(f'{operator=}')
        #print('--------------')
    return final_sum