# Solution for AoC 2022 Day 04 - Camp Cleanup

require 'set'

def input_per_line(file)
  File.readlines(file, chomp:true)
end


elf_pairs = input_per_line("../input.txt")
part_1_sum = 0
part_2_sum = 0
elf_pairs.each do |line|
  (left_elf, right_elf) = line.split(",") 
  (left_elf_start, left_elf_end) = left_elf.split("-")
  (right_elf_start, right_elf_end) = right_elf.split("-")
  left_elf_sections = (left_elf_start..left_elf_end).to_a.to_set
  right_elf_sections = (right_elf_start..right_elf_end).to_a.to_set
  if left_elf_sections.subset?(right_elf_sections) or right_elf_sections.subset?(left_elf_sections)
    part_1_sum += 1
  end
  if not left_elf_sections.disjoint?(right_elf_sections) or not right_elf_sections.disjoint?(left_elf_sections)
    part_2_sum += 1
  end

end

puts "The elves who have full subsets of the other total: #{part_1_sum}."
puts "The elves who have at least one section in common total: #{part_2_sum}."
