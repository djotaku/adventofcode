required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def evaluate_passport_fields(credentials):
    keys = set(credentials.keys())
    if required_fields - keys == set() or required_fields - keys == {'cid'}:
        return True
    else:
        return False


def check_birth_year(passport):
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False
    else:
        return True


def check_issue_year(passport):
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False
    else:
        return True


def check_expiration_year(passport):
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False
    else:
        return True


def check_height(height_info):
    if height_info[1] == "in":
        if 59 <= int(height_info[0]) <= 76:
            return True
    if height_info[1] == "cm":
        if 150 <= int(height_info[0]) <= 193:
            return True


def check_hair_color(passport):
    if passport['hcl'][0] != "#":
        return False
    elif len(passport['hcl']) != 7:
        return False
    else:
        return True


def check_eye_color(passport):
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if passport['ecl'] in valid_eye_colors:
        return True
    else:
        return False


def check_pid(passport):
    if len(passport['pid']) != 9:
        return False
    if passport['pid'].isnumeric():
        return True
    else:
        return False


def validate_passport_values(passport):
    height_parsing = [passport['hgt'][:-2], passport['hgt'][-2:]]

    return check_birth_year(passport) and check_issue_year(passport) and check_height(height_parsing) and \
           check_expiration_year(passport) and check_hair_color(passport) and check_eye_color(passport) and \
           check_pid(passport)


with open("input", 'r') as file:
    count = 0
    credentials = {}
    for line in file:
        if line != "\n":
            ready_for_dict = [item.split(":") for item in line.split()]
            # can't do credentials = credentials | dict(ready_for_dict) since I don't have 3.9....
            credentials.update(dict(ready_for_dict))
        else:
            if evaluate_passport_fields(credentials):
                if validate_passport_values(credentials):
                    count += 1
            credentials.clear()

print(count)

# 128 is too high
