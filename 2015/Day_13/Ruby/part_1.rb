require "../../input_parsing/parse_input"

def create_guest_hash(lines)
    guest_hash = Hash.new
    lines.each do | line |
        people_and_values = line.scan(/(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\./)
        if !guest_hash.has_key?(people_and_values[0][0])
            guest_hash[people_and_values[0][0]] = {}
        end
        number = people_and_values[0][1] == "lose" ? "-#{people_and_values[0][2]}" : "#{people_and_values[0][2]}"
        guest_hash[people_and_values[0][0]][people_and_values[0][3]] = number
    end
    guest_hash
end
