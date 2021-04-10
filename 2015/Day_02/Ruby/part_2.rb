require "../../input_parsing/parse_input"

def get_dimensions(dimension_line)
    dimensions = dimension_line.split('x')
    dimensions.map(&:to_i)
end


def calculate_bow_length(dimensions)
    dimensions[0]*dimensions[1]*dimensions[2]
end

def calculate_ribbon_length(dimensions)
    sorted_dimensions = dimensions.sort
    2* sorted_dimensions[0] + 2 * sorted_dimensions[1]
end
    

if $PROGRAM_NAME == __FILE__
    input_text = input_per_line('../input.txt')
    all_ribbon_lengths = []
    all_bow_lengths = []
    input_text.each do |box|
        all_ribbon_lengths.append(calculate_ribbon_length(get_dimensions(box)))
        all_bow_lengths.append(calculate_bow_length(get_dimensions(box)))
    end

    summed_ribbon_lengths = all_ribbon_lengths.reduce(0) {|sum, num| sum + num}
    summed_bow_lengths = all_bow_lengths.reduce(0) {|sum, num| sum + num}

    puts "The Elves need #{summed_ribbon_lengths+summed_bow_lengths} feet of ribbon!"
end
