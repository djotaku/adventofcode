require "../../input_parsing/parse_input"

depths = input_per_line("../input.txt")
answer_one = depths.map(&:to_i).each_cons(2).map{|a, b| a < b ? 1 : 0}.reduce(:+)
puts "There are #{answer_one} measurements larger than the previous one."
answer_two = depths.map(&:to_i).each_cons(3).map{|a, b, c| a + b + c}.each_cons(2).map{|a, b| a < b ? 1 : 0}.reduce(:+)
puts "There are #{answer_two} measurements larger than the previous one when considering 3 at a time."