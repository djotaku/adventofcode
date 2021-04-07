require "../../input_parsing/parse_input"

def parse_directions(parenthesis)
    parenthesis.reduce(0) do | floor, paren |
        if paren == "("
            floor + 1
        elsif paren == ")"
            floor - 1
        end
    end
end



input_text = input_per_line('../input.txt')
puts parse_directions(input_text[0].split(//))
