require "../../input_parsing/parse_input"

def create_dictionary(instructions)
    wires = Hash.new
    instructions.each do |instruction|
        match_results = instruction.scan(/(.*) -> (\w+)/)
        connection = match_results[0][0]
        wire = match_results[0][1]
        wires[wire] = connection
    end
    wires
end

def break_up_equation(equation)
    if equation.match?(/(\w+) ([A-Z]*) (\w+)/)
        broken_equation = equation.scan(/(\w+) ([A-Z]*) (\w+)/)
        return broken_equation[0][0], broken_equation[0][1], broken_equation[0][2]
    elsif equation.match?(/([A-Z]*) ([a-z]+)/)
        broken_equation = equation.scan(/([A-Z]*) ([a-z]+)/)
        return broken_equation[0][0], broken_equation[0][1]
    else
        return [equation]
    end
end

@all_wires = Hash.new

def find_value_on_line(wire_to_find)
    if Integer(@all_wires[wire_to_find], exception: false)
        return @all_wires[wire_to_find].to_i
    end
    equation = break_up_equation(@all_wires[wire_to_find])
    if equation.length() == 3
        if Integer(equation[0], exception: false)
            operand_left = equation[0].to_i
        else
            operand_left = find_value_on_line(equation[0])
        end
        if Integer(equation[2], exception: false)
            operand_right = equation[2].to_i
        else
            operand_right = find_value_on_line(equation[2])
        end
        operation = equation[1]
        if operation == "AND"
            return operand_left & operand_right
        elsif operation == "LHIFT"
            return operand_left << operand_right
        elsif operation == "OR"
            return operand_left | operand_right
        elsif operation == "RSHIFT"
            return operand_left >> operand_right
        end
    elsif equation.length() == 2
        return find_value_on_line(equation[1]) ^ 65535
    else
        return find_value_on_line(equation[0])
    end
end


if $PROGRAM_NAME == __FILE__
    instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g','NOT x -> h', 'NOT y -> i']
    @all_wires = create_dictionary(instructions)
    answer = find_value_on_line('d')
    puts answer
end
