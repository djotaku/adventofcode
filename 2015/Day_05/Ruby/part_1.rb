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
    line_to_evaluate.match?(/(.)\1/)
end

def rule_three(line_to_evaluate)
    ! line_to_evaluate.match?(/ab|cd|pq|xy/)
end

def naughty_or_nice(line_to_evaluate)
    !! rule_one(line_to_evaluate) and rule_two(line_to_evaluate) and rule_three(line_to_evaluate)
end
