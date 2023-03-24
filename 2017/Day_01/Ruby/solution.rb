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


captcha = input_per_line("../input.txt")
partOne = find_doubles(captcha[0])
puts partOne