def look_and_say_round(game_input)
    game_input_array = game_input.split(//)
    game_input_array.chunk_while { |a, b| a == b }
    .flat_map { |chunk| "#{chunk.size}#{chunk.first}" }
    .join('')
end


if $PROGRAM_NAME == __FILE__
    input = "1321131112"
    puts "#{look_and_say_round(input)}"
end

