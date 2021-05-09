require "../../input_parsing/parse_input"

def find_numbers(line)
    numbers = line.scan(/(-*\d+)/).flat_map {|e| e}
end

def sum_numbers(numbers)
    numbers.reduce(0) {|sum, num| sum + num.to_i}
end

if $PROGRAM_NAME == __FILE__
   lines  = input_per_line('../input.txt')
   line_totals = []
   lines.each do | line |
       line_totals.append(sum_numbers(find_numbers(line)))
   end
   final_total = line_totals.reduce(0) {|sum, num| sum + num}
   puts "The Final sum of all the numbers is #{final_total}"
end
