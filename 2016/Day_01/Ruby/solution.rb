require "../../input_parsing/parse_input"
require 'set'

direction = Complex(0, 1)
location = [0, 0]
visited_locations = Set[[0,0]]
part_two_location = [0,0]
keep_searching_part_two = true

directions_to_bunny_hq = input_per_line("../input.txt")
parsed_directions = directions_to_bunny_hq[0].split(/,/)
parsed_directions.each do |orientation_steps|
  regex = orientation_steps.scan(/(\w)(\d+)/)
  puts orientation_steps
  if regex[0][0] == "L"
    print("left: ")
    direction *= Complex('i')
  else
    direction *= -Complex('i')
  end
  blocks = regex[0][1]
  puts blocks
  puts direction
  (0...blocks.to_i).each do
    location[0] += direction.real
    location[1] += direction.imaginary
    if visited_locations.include? [location[0], location[1]] and keep_searching_part_two
      part_two_location = [location[0], location[1]]
      keep_searching_part_two = false
    else
      visited_locations.add([location[0], location[1]])
    end
  end
end

distance_part_1 = location[0].abs + location[1].abs
distance_part_2 = part_two_location[0].abs + location[1].abs

puts "The distance to Easter Bunny HQ is #{distance_part_1} according to part 1."
puts "The distance to Easter Bunny HQ is #{distance_part_2} according to part 2."