require "../../input_parsing/parse_input"

container_sizes = input_per_line("../input.txt")
container_combinations = []
container_sizes = container_sizes.map{|x| x.to_i}
container_combinations = (1..container_sizes.length).to_a.each{|x| container_sizes.combination(x)}.map{|y| y if y.sum == 150}
#container_combinations = container_combinations.compact.reject(&:empty?)
print container_combinations