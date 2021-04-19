require "../../input_parsing/parse_input"

def generate_coordinates(starting_coordinate, ending_coordinate)
    starting_x = starting_coordinate[0]
    starting_y = starting_coordinate[1]
    ending_x = ending_coordinate[0]
    ending_y = ending_coordinate[1]
    coordinates = []
    (starting_x..ending_x).each do |x|
        (starting_y..ending_y).each do |y|
            coordinates.append([x,y])
        end
    end
    coordinates
end

def get_coordinates_from_text(instruction)
    instruction.scan(/(\d*),(\d*)/)
end

def run_the_lightshow(instructions)
    lights = Hash.new
    instructions.each do |instruction|
        corners = get_coordinates_from_text(instruction)
        starting_x  = corners[0][0].to_i
        starting_y  = corners[0][1].to_i
        ending_x = corners[1][0].to_i
        ending_y = corners[1][1].to_i
        coordinates = generate_coordinates([starting_x,starting_y],[ending_x,ending_y])
        coordinates.each do |coordinate|
            if instruction.include?("turn on")
                lights[coordinate.to_s] = 1
            elsif instruction.include?("turn off")
                lights[coordinate.to_s] = 0
            elsif instruction.include?("toggle")
                if lights.include?(coordinate.to_s)
                    lights[coordinate.to_s] ^= 1
                else
                    lights[coordinate.to_s] = 1
                end
            else
                puts "If I get here, something has gone wrong."
            end
        end
        
    end
   lights.values.reduce(0) {|sum, num| sum + num}
end


if $PROGRAM_NAME == __FILE__
    light_show_instructions = input_per_line('../input.txt')
    lights_on = run_the_lightshow(light_show_instructions)
    puts "Thanks to Santa, we have a crazy light bill because #{lights_on} are on!"
end
