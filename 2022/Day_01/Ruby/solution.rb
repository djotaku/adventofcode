# Solution to 2022 Day 01 - Calorie Counting

def input_per_line(file)
  File.readlines(file, chomp:true)
end

elf_calorie_list = input_per_line("../input.txt")
calorie_per_elf = elf_calorie_list.map(&:to_i).slice_when {|i, j| j==0}.to_a
elf_sum = []
calorie_per_elf.each do |item|
  elf_sum.append(item.sum)
end
elf_sum.sort!.reverse!

puts "The elf with the highest amount of calories is carrying #{elf_sum[0]} calories. "

puts "The top 3 elves with the highest amount of calories are carrying #{elf_sum[0]+elf_sum[1]+elf_sum[2]} calories. "