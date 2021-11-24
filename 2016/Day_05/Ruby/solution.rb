require 'digest'

def create_hash(text)
    Digest::MD5.hexdigest text
end


def start_with_five_zeroes(hash_to_test)
    hash_to_test[0..4] == "00000"
end

def find_number_part_one(secret_key)
    number = 1
    password_hash = secret_key + number.to_s
    door_one = ""
    until door_one.length == 8
        until start_with_five_zeroes(create_hash(password_hash))
            number += 1
            password_hash = secret_key + number.to_s
        end
        this_hash = create_hash(password_hash)
        door_one += this_hash[5]
        number += 1
        password_hash = secret_key + number.to_s
    end
    door_one
end

def find_number_part_two(secret_key)
    number = 1
    password_hash = secret_key + number.to_s
    door_two = ["", "", "", "", "", "", "", ""]
    while door_two.include? ""
        until start_with_five_zeroes(create_hash(password_hash))
            number += 1
            password_hash = secret_key + number.to_s
        end
        this_hash = create_hash(password_hash)
        # puts this_hash
        if this_hash[5].match(/\d/)
            if this_hash[5].to_i < 8
                if door_two[this_hash[5].to_i] == ""
                    door_two[this_hash[5].to_i] = this_hash[6]
                end
            end
        end
        number += 1
        password_hash = secret_key + number.to_s
        puts "#{door_two}"
    end
    door_two
end

if $PROGRAM_NAME == __FILE__
  input = "ugkcyxxp"
  door_one = find_number_part_one(input)
  puts "The password to the first door is: #{door_one}.\n"
  door_two = find_number_part_two(input)
  puts "The answer to the second door is #{door_two}."
end