require "../../input_parsing/parse_input"

def parse_directions(parenthesis)
    floor = 0
    parenthesis.each do |paren|
    if paren == "("
        floor += 1
    elsif paren == ")"
        floor -= 1
    end
    end
    return floor
end



input_text = input_per_line('../input.txt')
puts parse_directions(input_text[0].split(//))
