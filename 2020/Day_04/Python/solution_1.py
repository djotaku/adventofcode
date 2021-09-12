required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}


def evaluate_passport(credentials):
    keys = set(credentials.keys())
    if required_fields - keys == set() or required_fields - keys == {'cid'}:
        return True
    else:
        return False


with open("input", 'r') as file:
    count = 0
    credentials = {}
    for line in file:
        if line != "\n":
            ready_for_dict = [item.split(":") for item in line.split()]
            # can't do credentials = credentials | dict(ready_for_dict) since I don't have 3.9....
            credentials.update(dict(ready_for_dict))
        else:
            if(evaluate_passport(credentials)):
                count += 1
            credentials.clear()

print(count)
