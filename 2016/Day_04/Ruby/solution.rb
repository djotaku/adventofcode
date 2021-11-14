require "../../input_parsing/parse_input"

def count_and_sort_letters(room_string)
  room_string.scan(/[a-z]/).tally.to_a.sort_by!{|character| [-character[1], character[0]]}[0..4]
end

print count_and_sort_letters("hello goodbye")