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
