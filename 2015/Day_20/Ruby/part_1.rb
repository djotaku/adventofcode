PRESENTS_DELIVERED = 34000000

house_list = Array.new((PRESENTS_DELIVERED/10), 0)

for i in (1...(PRESENTS_DELIVERED/10)) do
    for j in (i...(PRESENTS_DELIVERED/10)).step(i) do
        house_list[j] += i * 10
    end
end


for house in house_list
    if house >= PRESENTS_DELIVERED
        puts "House is #{house}"
        break
    end
end
