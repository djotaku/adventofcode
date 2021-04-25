require "../../input_parsing/parse_input"

def count_code_rep(line)
    line.length
end

def count_in_memory_string(line)
    line_length = line.length
    line_no_outer_quotes = line.delete_prefix('"')
    line_no_outer_quotes = line.delete_suffix('"')
    subtraction_count = 2
    line_no_outer_quotes.scan(/(\\\\)|(\\["])|(\\x[0-9a-f]{2})/) do | a_match |
        a_match.each do | backspace_or_unicode |
            if backspace_or_unicode == nil
            elsif backspace_or_unicode.match?(/(\\\\)|(\\["])/)
                subtraction_count += 1
            elsif backspace_or_unicode.match?(/\\x[0-9a-f]{2}/)
                subtraction_count +=3
            end
        end
    end
    line_length - subtraction_count
end

if $PROGRAM_NAME == __FILE__
    strings = input_per_line('../input.txt')
    code_rep_length = []
    memory_string_length = []
    strings.each do | line |
        code_rep_length.append(count_code_rep(line))
        memory_string_length.append(count_in_memory_string(line))
    end
    sum_code_rep = code_rep_length.reduce(0) { |sum, num| sum + num}
    sum_memory_string = memory_string_length.reduce(0) { |sum, num| sum + num}
    puts "sum_code_rep is #{sum_code_rep}"
    puts "sum_memory_string is #{sum_memory_string}"
    puts "Answer is #{sum_code_rep - sum_memory_string}"
end
