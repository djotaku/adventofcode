PRESENTS_DELIVERED = 34000000

house_list = Array.new((PRESENTS_DELIVERED/10), 0)

(1...(PRESENTS_DELIVERED / 10)).each { |i|
    (i...(PRESENTS_DELIVERED / 10)).step(i).each { |j|
        house_list[j] += i * 10
    }
}

house_list.each_with_index { |house, house_number|
    if house >= PRESENTS_DELIVERED
        puts "House is #{house_number}"
        break
    end
}
