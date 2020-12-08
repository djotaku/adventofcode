import re
bags = {}
seen = set()
count = 0
file = open('input',mode='r')
for line in file.read().split(".\n"):
    line = re.sub("(bags|bag)","",line)
    line = line.replace(".","")
    key, values = line.split(" contain ")
    if 'no other' in values:
        bags[key.strip()] = {}
    else:
        bags[key.strip()] = {bag: int(time) for time, bag in (value.strip().split(" ", 1) for value in values.split(", "))}