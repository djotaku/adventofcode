def look_and_say_round(game_input)
    game_input_array = game_input.split(//)
    game_input_array.chunk_while { |a, b| a == b }
    .flat_map { |chunk| "#{chunk.size}#{chunk.first}" }
    .join('')
end


if $PROGRAM_NAME == __FILE__
    input = "1321131112"
    loop_count = 0
    until loop_count == 50
        puzzle_output = look_and_say_round(input)
        input = puzzle_output
        loop_count += 1
    end
    puts "Length of output after 40 roundes of look and say is #{puzzle_output.length}"
end

