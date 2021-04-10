require "../../input_parsing/parse_input"
require 'set'

def separate_directions(direction_line)
    direction_line.split(//)
end

def count_houses_visited(directions)
    set_of_houses = Set[[0,0]]
    santa_current_coordinate = [0,0]
    robo_santa_current_coordinate = [0,0]
    count = 0
    directions.each do |direction|
        if direction == "^"
            if count == 0 or count % 2 == 0
                santa_current_coordinate[1] += 1
                set_of_houses.add([santa_current_coordinate[0], santa_current_coordinate[1]])
            else
                robo_santa_current_coordinate[1] += 1
                set_of_houses.add([robo_santa_current_coordinate[0], robo_santa_current_coordinate[1]])
            end
        elsif direction =="v"
            if count == 0 or count % 2 == 0
                santa_current_coordinate[1] -= 1
                set_of_houses.add([santa_current_coordinate[0], santa_current_coordinate[1]])
            else
                robo_santa_current_coordinate[1] -= 1
                set_of_houses.add([robo_santa_current_coordinate[0], robo_santa_current_coordinate[1]])
            end
        elsif direction == "<"
            if count == 0 or count % 2 == 0
                santa_current_coordinate[0] -= 1
                set_of_houses.add([santa_current_coordinate[0], santa_current_coordinate[1]])
            else
                robo_santa_current_coordinate[0] -= 1
                set_of_houses.add([robo_santa_current_coordinate[0], robo_santa_current_coordinate[1]])
            end
        elsif direction == ">"
            if count == 0 or count % 2 == 0
                santa_current_coordinate[0] += 1
                set_of_houses.add([santa_current_coordinate[0], santa_current_coordinate[1]])
            else
                robo_santa_current_coordinate[0] += 1
                set_of_houses.add([robo_santa_current_coordinate[0], robo_santa_current_coordinate[1]])
            end
        end
        count += 1
    end
    set_of_houses.length()
end

if $PROGRAM_NAME == __FILE__
    input_text = input_per_line('../input.txt')
    santas_directions = separate_directions(input_text[0])
    puts "#{count_houses_visited(santas_directions)} houses were visited at least once by Santa or Robo-Santa."
end
