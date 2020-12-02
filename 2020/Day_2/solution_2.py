with open("input", 'r') as file:
    passwords_for_evaluation = [line.split() for line in file.readlines()]

correct_password_count = []

for password_and_policy in passwords_for_evaluation:
    positions = password_and_policy[0].split('-')
    letter = password_and_policy[1][0]
    password = password_and_policy[2]
    if password[int(positions[0])-1] == letter:
        if password[int(positions[1])-1] != letter:
            correct_password_count.append(True)
    elif password[int(positions[1])-1] == letter:
        correct_password_count.append(True)

print(correct_password_count.count(True))
