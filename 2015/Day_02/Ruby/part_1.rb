require "../../input_parsing/parse_input"

def get_dimensions(dimension_line)
    dimensions = dimension_line.split('x')
    dimensions.map(&:to_i)
end


def calculate_box_area(dimensions)
    2*dimensions[0]*dimensions[1] + 2*dimensions[1]*dimensions[2] + 2*dimensions[0]*dimensions[2] 
end

def calculate_small_area(dimensions)
    sorted_dimensions = dimensions.sort
    small_area = sorted_dimensions[0] * sorted_dimensions[1]
end
    

input_text = input_per_line('../input.txt')
all_box_areas = []
all_small_areas = []
input_text.each do |box|
    all_box_areas.append(calculate_box_area(get_dimensions(box)))
    all_small_areas.append(calculate_small_area(get_dimensions(box)))
end

summed_box_areas = all_box_areas.reduce(0) {|sum, num| sum + num}
summed_small_areas = all_small_areas.reduce(0) {|sum, num| sum + num}

puts "The Elves need #{summed_box_areas+summed_small_areas} square feet of wrapping paper!"
