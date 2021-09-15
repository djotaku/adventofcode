PRESENTS_DELIVERED = 34000000

house_dict = {}

for i in range(1, (PRESENTS_DELIVERED//10)):
    for j in range(i, PRESENTS_DELIVERED//10, i):
        if j in house_dict:
            house_dict[j] += i * 10
        else:
            house_dict[j] = 10

for key, value in house_dict.items():
    if value >= PRESENTS_DELIVERED:
        print(f"House is {key}")
        break
