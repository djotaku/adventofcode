require "../../input_parsing/parse_input"

def create_sue_hash(sue_value_list)
  sue_hash = Hash.new
  sue_value_list.each do |aunt|
    important_values = aunt.scan(/Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)/)
    sue_hash = {important_values[0][0]=>{important_values[0][1]=>important_values[0][2],important_values[0][3]=>important_values[0][4], important_values[0][5]=>important_values[0][6]}}
  end
  sue_hash
end


if $PROGRAM_NAME == __FILE__
  sue_list = input_per_line('../input.txt')
  sue_hash = create_sue_hash(sue_list)
  puts sue_hash
  puts sue_hash
end