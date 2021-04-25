require "../../input_parsing/parse_input"

def count_code_rep(line)
    line.length
end

def count_encode(line)
    line_length = line.length
    encode_count = 2  # this is for the extra double-quotes added as part of the part2 encoding scheme
    chars_that_need_backslash = line.count '"\\'
    line_length + encode_count + chars_that_need_backslash
end

if $PROGRAM_NAME == __FILE__
    strings = input_per_line('../input.txt')
    code_rep_length = []
    encode_string_length = []
    strings.each do | line |
        code_rep_length.append(count_code_rep(line))
        encode_string_length.append(count_encode(line))
    end
    sum_code_rep = code_rep_length.reduce(0) { |sum, num| sum + num}
    sum_encode_string = encode_string_length.reduce(0) { |sum, num| sum + num}
    puts "Answer is #{sum_encode_string - sum_code_rep}"
end
