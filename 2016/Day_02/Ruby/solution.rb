require "../../input_parsing/parse_input"
require 'set'

KEYPAD_PART_1 = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]

KEYPAD_PART_2 = [[0, 0, 1, 0, 0],
                 [0, 2, 3, 4, 0],
                 [5, 6, 7, 8, 9],
                 [0, "A", "B", "C", 0],
                 [0, 0, "D", 0, 0]]

VALID_KEYS_PART_1 = Set[[0,0], [0, 1], [0, 2],
                        [1,0], [1, 1], [1, 2],
                        [2,0], [2, 1], [2, 2]]

VALID_KEYS_PART_2 = Set[[0, 2],
                        [1, 1], [1, 2], [1, 3],
                        [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                        [3, 1], [3, 2], [3, 3],
                        [4, 2]]

def find_next_key(outer_matrix, inner_matrix, directions_this_key, part)
  this_outer_matrix = outer_matrix
  this_inner_matrix = inner_matrix
  if part == 1
    this_keypad = KEYPAD_PART_1
    this_valid_keys = VALID_KEYS_PART_1
  else
    this_keypad = KEYPAD_PART_2
    this_valid_keys = VALID_KEYS_PART_2
  end
  directions_this_key.each do |direction|
    case direction
    when "U"
      if this_valid_keys.include?([(this_outer_matrix - 1), this_inner_matrix])
        this_outer_matrix -= 1
      end
    when "D"
      if this_valid_keys.include?([(this_outer_matrix + 1), this_inner_matrix])
        this_outer_matrix += 1
      end
    when "L"
      if this_valid_keys.include?([this_outer_matrix, (this_inner_matrix - 1)])
        this_inner_matrix -= 1
      end
    when "R"
      if this_valid_keys.include?([this_outer_matrix, (this_inner_matrix + 1)])
        this_inner_matrix += 1
      end
    else
      "Should not get here"
    end
  end
  [this_keypad[this_outer_matrix][this_inner_matrix], this_outer_matrix, this_inner_matrix]
end

keypad_instructions = input_per_line("../input.txt")
part_one_inner_matrix = 1
part_one_outer_matrix = 1
part_one_code = ""
keypad_instructions.each do |instruction|
  instruction = instruction.split("")
  answer = find_next_key(part_one_outer_matrix, part_one_inner_matrix, instruction,1)
  part_one_code += answer[0].to_s
  part_one_outer_matrix = answer[1]
  part_one_inner_matrix = answer[2]
end

part_two_inner_matrix = 0
part_two_outer_matrix = 2
part_two_code = ""
keypad_instructions.each do |instruction|
  instruction = instruction.split("")
  answer = find_next_key(part_two_outer_matrix, part_two_inner_matrix, instruction,2)
  part_two_code += answer[0].to_s
  part_two_outer_matrix = answer[1]
  part_two_inner_matrix = answer[2]
end

puts "The supposed code is #{part_one_code}. The actual code is #{part_two_code}"