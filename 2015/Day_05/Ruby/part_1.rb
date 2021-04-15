require "../../input_parsing/parse_input"


def rule_one(line_to_evaluate)
    vowel_count = 0
    line_to_evaluate.scan(/[aeiou]/) do 
        vowel_count += 1
    end
    if vowel_count >= 3
        return true
    end
end


def rule_two(line_to_evaluate)
    line_to_evaluate.match(/(.)/)
end
