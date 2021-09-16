PUZZLE_INPUT = 34000000

def presents_per_house(house_number)
  presents = []
  (1..50).each do |elf|
    if house_number % elf == 0
      presents.append(house_number/elf)
    end
  end
  11 * presents.sum
end

house_number = 786240
presents_delivered = 0
until presents_delivered >= PUZZLE_INPUT
  presents_delivered = presents_per_house(house_number)
  house_number += 1
end

puts "The lowest house number is #{house_number-1}."