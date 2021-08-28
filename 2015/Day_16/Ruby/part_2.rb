require "../../input_parsing/parse_input"

def create_sue_hash(sue_value_list)
  sue_hash = Hash.new
  sue_value_list.each do |aunt|
    important_values = aunt.scan(/Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)/)
    sue_hash[important_values[0][0]] = {important_values[0][1]=>important_values[0][2],important_values[0][3]=>important_values[0][4], important_values[0][5]=>important_values[0][6]}
  end
  sue_hash
end


if $PROGRAM_NAME == __FILE__
  sue_list = input_per_line('../input.txt')
  sue_hash = create_sue_hash(sue_list)
  sue_hash.keep_if{|key, value| value["children"] == '3' or value["children"] == nil}
  sue_hash.keep_if{|key, value| value["cats"] == nil or value["cats"].to_i > 7 }
  sue_hash.keep_if{|key, value| value["samoyeds"] == '2' or value["samoyeds"] == nil }
  sue_hash.keep_if{|key, value| value["pomeranians"] == nil or value["pomeranians"].to_i < 3}
  sue_hash.keep_if{|key, value| value["akitas"] == '0' or value["akitas"] == nil }
  sue_hash.keep_if{|key, value| value["vizslas"] == '0' or value["vizslas"] == nil }
  sue_hash.keep_if{|key, value| value["goldfish"] == nil or value["goldfish"].to_i < 5 }
  sue_hash.keep_if{|key, value| value["trees"] == nil or value["trees"].to_i > 3}
  sue_hash.keep_if{|key, value| value["cars"] == '2' or value["cars"] == nil }
  sue_hash.keep_if{|key, value| value["perfumes"] == '3' or value["perfumes"] == nil }
  puts sue_hash
end