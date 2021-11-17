require "../../input_parsing/parse_input"

def count_and_sort_letters(room_string)
  room_string.scan(/[a-z]/).tally.to_a.sort_by!{|character| [-character[1], character[0]]}[0..4]
end

def valid_sector_id(character_count, checksum)
  character_count.map.with_index { |character, index| character[0] == checksum[index]}.all?
end

def letter_mover(letter, number)
  (0...number).each do
    if letter == "z"
      letter = "a"
    else
      letter = letter.next
    end
  end
  letter
end

def decryptor(encrypted_room, sector_id)
  shift_amount = sector_id.to_i % 26
  decrypted = encrypted_room.chars.map{|letter| letter_mover(letter, shift_amount)}.join
  puts decrypted
  if decrypted.include? "object"
    true
  else
    false
  end
end

encrypted_rooms = input_per_line("../input.txt")
sector_id_sum = 0
part_two_sector_id = 0
encrypted_rooms.each do |room|
  encrypted_part = room.scan(/(\w+-)/).join
  character_counts = count_and_sort_letters(encrypted_part)
  sector_and_checksum = room.scan(/(\d+)\[(\w+)\]/)
  if valid_sector_id(character_counts, sector_and_checksum[0][1])
    sector_id_sum += sector_and_checksum[0][0].to_i
    if decryptor(encrypted_part, sector_and_checksum[0][0])
      part_two_sector_id = sector_and_checksum[0][0]
    end
  end
end

puts "The sum of the sector IDs of the real rooms: #{sector_id_sum}"
puts "The decrypted room has a sector ID of #{part_two_sector_id}."