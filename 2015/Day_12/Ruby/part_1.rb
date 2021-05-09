require "../../input_parsing/parse_input"

def find_numbers(line)
    line.scan(/(-*\d+)/)
end

def sum_numbers(numbers)
    numbers.reduce(0) {|sum, num| sum + num}
end

if $PROGRAM_NAME == __FILE__
   lines  = input_per_line('../input.txt')
   line_totals = []
   
end
