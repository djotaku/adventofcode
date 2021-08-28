require "../../input_parsing/parse_input"

container_sizes = input_per_line("../input.txt")
container_combinations = []
container_sizes = container_sizes.map{|x| x.to_i}
(1..container_sizes.length).each do|x|
  container_combinations.append(container_sizes.combination(x)
                                 .map{|y| y if y.sum == 150}
                                 .compact)
end
container_combinations = container_combinations.compact.reject(&:empty?).flatten(1)
puts container_combinations.length