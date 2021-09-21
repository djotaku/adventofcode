require "../../input_parsing/parse_input"

packages = input_per_line("../input.txt")
#packages = [1,2,3,4,5,7,8,9,10,11]
packages = packages.map{|x| x.to_i}
package_combinations = (1..packages.length).map{|x| packages.combination(x).map{|y| y if y.sum == packages.sum/3}.compact}
                                           .compact
                                           .reject(&:empty?)
                                           .flatten(1)
santa_leg_room_packages = 100000000000000000
package_combinations.each {|combination| santa_leg_room_packages = [santa_leg_room_packages, combination.length].min}
group_1_contenders = package_combinations.map {|combination| combination if combination.length == santa_leg_room_packages}
                                         .compact
if group_1_contenders.length == 1
  puts "The quantum entanglement of the packages in Santa's leg area is #{group_1_contenders[0].reduce(1){|prod, num| prod * num}}"
else
  quantum_entanglement = 10000000000000000000000
  group_1_contenders.each{|contender| quantum_entanglement = [quantum_entanglement, contender.reduce(1){|prod, num| prod * num}].min}
  puts "The quantum entanglement of the packages in Santa's leg area is #{quantum_entanglement}}"
end