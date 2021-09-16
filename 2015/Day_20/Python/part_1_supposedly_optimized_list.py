PRESENTS_DELIVERED = 34000000

house_list = [0] * (PRESENTS_DELIVERED//10)

for i in range(1, (PRESENTS_DELIVERED//10)):
    for j in range(i, PRESENTS_DELIVERED//10, i):
        if house_list[j] == 0:
            house_list[j] = 10
        else:
            house_list[j] += i * 10

for house_number, house in enumerate(house_list):
    if house >= PRESENTS_DELIVERED:
        print(f"House is {house_number}")
        break
