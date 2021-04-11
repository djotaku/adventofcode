require 'digest'

def create_hash(text)
    Digest::MD5.hexdigest text
end


def start_with_five_zeroes(hash_to_test)
    hash_to_test[0..4] == "00000"
end

def find_number(secret_key)
    number = 0
    adventcoin = secret_key + number.to_s
    until start_with_five_zeroes(create_hash(adventcoin))
        number += 1
        adventcoin = secret_key + number.to_s
    end
    return number
end

if $PROGRAM_NAME == __FILE__
    input = "iwrupvqb"
    the_number = find_number(input)
    puts "Santa's number is #{the_number}"
end
