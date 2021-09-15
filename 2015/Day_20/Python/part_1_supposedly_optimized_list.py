PRESENTS_DELIVERED = 34000000

house_list = []

for i in range(1, (PRESENTS_DELIVERED//10)):
    for j in range(i, PRESENTS_DELIVERED//10, i):
        if j in house_list:
            house_list[j] += i * 10

for house in house_list:
    if house >= PRESENTS_DELIVERED:
        print(f"House is {house}")
        break
