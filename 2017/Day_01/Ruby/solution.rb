# frozen_string_literal: true

def input_per_line(file)
  File.readlines(file, chomp:true)
end

def find_doubles(numbers)
  regex = numbers.scan(/(\d)(?=\1)/)
  sum = regex.flatten.map(&:to_i).each.reduce(0){|sum, num| sum + num}
  if numbers[0] == numbers[-1]
    sum += numbers[0].to_i
  end
  sum
end


def find_doubles_part2(numbers)
  look_ahead = numbers.length / 2
  number_sum = 0
  numbers.split("").each_with_index do |number, index|
    check_index = (index + look_ahead) % numbers.length
    if number == numbers[check_index]
      number_sum += number.to_i
    end
  end
  number_sum
end

captcha = input_per_line("../input.txt")
part_one = find_doubles(captcha[0])
puts part_one
part_two = find_doubles_part2(captcha[0])
puts part_two