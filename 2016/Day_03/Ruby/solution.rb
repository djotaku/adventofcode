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
triangle_2_creator_count = 0

triangle_triples_input.each do |triple|
  this_triple = triple.split(" ")
  triangle_count_part_1 += is_a_triangle(this_triple[0].to_i, this_triple[1].to_i, this_triple[2].to_i)
  triangle_part_two_array.append(this_triple)
  triangle_2_creator_count += 1
  if triangle_2_creator_count % 3 == 0
    transposed_triples = triangle_part_two_array.transpose
    transposed_triples.each do |trans_triple|
      triangle_count_part_2 += is_a_triangle(trans_triple[0].to_i, trans_triple[1].to_i, trans_triple[2].to_i)
    end
    triangle_part_two_array.clear
  end
end

puts "If we are looking at rows of triples, there are #{triangle_count_part_1} triangles"

puts "If we are looking at columns of triples, there are #{triangle_count_part_2} triangles"