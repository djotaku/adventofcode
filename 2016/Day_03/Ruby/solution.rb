require "../../input_parsing/parse_input"

def is_a_triangle(side_1, side_2, side_3)
  if side_1 + side_2 > side_3 and side_2 + side_3 >  side_1 and side_1 + side_3 > side_2
    1
  else
    0
  end
end

triangle_triples_input = input_per_line("../input.txt")
triangle_count_part_1 = 0
triangle_count_part_2 = 0
triangle_part_two_array = []

triangle_triples_input.each do |triple|
  this_triple = triple.split(" ")
  triangle_count_part_1 += is_a_triangle(this_triple[0].to_i, this_triple[1].to_i, this_triple[2].to_i)
end

puts "If we are looking at rows of triplets, there are #{triangle_count_part_1} triangles"

