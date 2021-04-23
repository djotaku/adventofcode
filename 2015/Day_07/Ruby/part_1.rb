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
        #puts "A 3 way match: #{broken_equation[0][0]}, #{broken_equation[0][1]}, #{broken_equation[0][2]}"
        return broken_equation[0][0], broken_equation[0][1], broken_equation[0][2]
    elsif equation.match?(/([A-Z]*) ([a-z]+)/)
        broken_equation = equation.scan(/([A-Z]*) ([a-z]+)/)
        #puts "A 2 way match: #{broken_equation[0][0]}, #{broken_equation[0][1]}"
        return broken_equation[0][0], broken_equation[0][1]
    else
        return [equation]
    end
end

@all_wires = Hash.new
@cache = Hash.new

def for_cache(wire_to_find)
#def find_value_on_line(wire_to_find)
    int = Integer(@all_wires[wire_to_find], exception: false)
    return int if int
    #puts "#{@all_wires[wire_to_find]}"
    equation = break_up_equation(@all_wires[wire_to_find])
    #puts "equation is #{equation[0]} #{equation[1]} #{equation[2]}"
    if equation.length() == 3
        operand_left = Integer(equation[0], exception: false)
        if operand_left
            #puts "L: #{operand_left} is a number"
        else
            #puts "L: #{equation[0]} is not a number"
            operand_left = find_value_on_line(equation[0])
            #puts "Now operand_left is #{operand_left}"
        end
        operand_right = Integer(equation[2], exception: false)
        if operand_right
            #puts "R: #{operand_right} is a number"
        else
            #puts "R: #{equation[2]} is not a number"
            operand_right = find_value_on_line(equation[2])
            #puts "Now operand_right is #{operand_right}"
        end
        operation = equation[1]
        if operation == "AND"
            return operand_left & operand_right
        elsif operation == "LSHIFT"
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

def find_value_on_line(wire_to_find)
    #puts "Cache value is #{@cache[wire_to_find]}"
    @cache[wire_to_find] ||= for_cache(wire_to_find)
end


if $PROGRAM_NAME == __FILE__
    instructions = input_per_line('../input.txt')
    #instructions = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g','NOT x -> h', 'NOT y -> i']
    @all_wires = create_dictionary(instructions)
    answer = find_value_on_line('a')
    #answer = for_cache('a')
    puts answer
end
