with open("input", 'r') as file:
    passwords_for_evaluation = [line.split() for line in file.readlines()]

correct_password_count = []

for password_and_policy in passwords_for_evaluation:
    repetitions = password_and_policy[2].count(password_and_policy[1][0])
    min_and_max = password_and_policy[0].split('-')
    if int(min_and_max[0]) <= repetitions <= int(min_and_max[1]):
        correct_password_count.append(True)

print(correct_password_count.count(True))
