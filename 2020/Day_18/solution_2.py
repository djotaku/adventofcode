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
            if isinstance(equation[index], list):
                equation[index] = evaluate_parenthesis(equation[index])
        return equation_with_parenthesis


def evaluate_plus(equation):
    """I will do a trick of adding parens around each summation"""
    for number in range(0, len(equation)):
        if equation[number] == "+":
            if equation[number-2] != "(":
                if equation[number-1] != ")":
                    if equation[number+1] != "(":
                        equation.insert(number-1, '(')
                        equation.insert(number+3, ')')
                        equation = evaluate_plus(equation)
                elif equation[number-1] == ")":
                    if equation[number + 1] != "(":
                        equation.insert(number+1, '(')
                        equation.insert(number + 3, ')')
                        equation = evaluate_plus(equation)
        elif isinstance(equation[number], list):
            if len(equation[number]) == 3 or len(equation[number]) == 1:
                pass
            else:
                equation[number] = evaluate_plus(equation[number])
                equation[number] = evaluate_parenthesis(equation[number])
                equation[number] = evaluate_plus(equation[number])
    print(equation)
    return equation


def parse_input(input_file):
    with open(input_file, 'r') as file:
        equations = [[char for char in line if char != ' '] for line in file.readlines()]
        parens_level_one = [evaluate_parenthesis(equation) for equation in equations]
        handle_plus_precedence = [evaluate_plus(equation) for equation in parens_level_one]
        fixed_equations = [evaluate_parenthesis(equation) for equation in handle_plus_precedence]
        return fixed_equations


def new_math(math_stack):
    final_sum = 0
    left_number = 0
    pocket_number = 0
    operator = ''
    for item in math_stack:
        if isinstance(item, list):
            if len(item) == 1:
                if not isinstance(item[0], list):
                    pocket_number = item[0]
            if left_number == 0:
                left_number = new_math(item)
                final_sum = left_number
            else:
                paren_sum = new_math(item)
                #print(f'{left_number}{operator}{paren_sum}')
                if pocket_number == 0:
                    final_sum = eval(f'{left_number}{operator}{paren_sum}')
                else:
                    final_sum = eval(f'{left_number}{operator}{paren_sum}+{pocket_number}')
                    pocket_number = 0
                left_number = final_sum
        elif item.isdigit():
            if left_number == 0:
                left_number = item
            else:
                #print(f'{item=}')
                #print(f'{left_number}{operator}{item}')
                final_sum = eval(f'{left_number}{operator}{item}')
                left_number = final_sum
        else:
            operator = item
        #print('--------')
        #print(f'{final_sum=}')
        #print(f'{left_number=}')
        #print('--------------')
    return final_sum


if __name__ == "__main__":
    my_equations = parse_input('input')
    answers = [new_math(equation) for equation in my_equations]
    print(f"The answer is {sum(answers)}")

# 85261204518763 is too low
# 54328280806251 is too low