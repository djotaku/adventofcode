require "../../input_parsing/parse_input"

def run_sub_commands(commands)
  horizontal = 0
  depth_part1 = 0
  depth_part2 = 0
  aim = 0
  commands.each do |command|
    direction_magnitude = command.split(/ /)
    magnitude = direction_magnitude[1].to_i
    case
    when direction_magnitude[0] == "forward"
      horizontal += magnitude
      depth_part2 += aim * magnitude
    when direction_magnitude[0] == "down"
      depth_part1 += magnitude
      aim += magnitude
    else
      depth_part1 -= magnitude
      aim -= magnitude
    end
  end
  [horizontal*depth_part1, horizontal*depth_part2]
end

sub_commands = input_per_line("../input.txt")
answers = run_sub_commands(sub_commands)
puts "You thought the right product was #{answers[0]}, but then you RTFM and realized it was #{answers[1]}"