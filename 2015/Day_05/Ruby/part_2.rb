require "../../input_parsing/parse_input"


def rule_one(line_to_evaluate)
    line_to_evaluate.match?(/(\w\w)\w*\1/)
end


def rule_two(line_to_evaluate)
    line_to_evaluate.match?(/(\w).\1/)
end

def naughty_or_nice(line_to_evaluate)
    !! rule_one(line_to_evaluate) and rule_two(line_to_evaluate)
end

if $PROGRAM_NAME == __FILE__
    naughty_or_nice_list = input_per_line('../input.txt')
    nice_count = 0
    naughty_or_nice_list.each do |line|
        if naughty_or_nice(line)
            nice_count += 1
        end
    end
    puts "Santa has #{nice_count} nice children."
end
