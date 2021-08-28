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
minimum_number_of_containers = container_combinations.map{|combination| combination.length}.min
min_container_combinations = container_combinations.map{|combination| combination if combination.length == minimum_number_of_containers }.compact
puts min_container_combinations.length