require "../../input_parsing/parse_input"
require 'set'

def separate_directions(direction_line)
    direction_line.split(//)
end

def count_houses_visited(directions)
    set_of_houses = Set[[0,0]]
    current_coordinate = [0,0]
    directions.each do |direction|
        if direction == "^"
            current_coordinate[1] += 1
            set_of_houses.add([current_coordinate[0], current_coordinate[1]])
        elsif direction =="v"
            current_coordinate[1] -= 1
            set_of_houses.add([current_coordinate[0], current_coordinate[1]])
        elsif direction == "<"
            current_coordinate[0] -= 1
            set_of_houses.add([current_coordinate[0], current_coordinate[1]])
        elsif direction == ">"
            current_coordinate[0] += 1
            set_of_houses.add([current_coordinate[0], current_coordinate[1]])
        end
    end
    set_of_houses.length()
end

if $PROGRAM_NAME == __FILE__
    input_text = input_per_line('../input.txt')
    santas_directions = separate_directions(input_text[0])
    puts "#{count_houses_visited(santas_directions)} houses were visited at least once by Santa."
end
