import re

pattern = r'aaaabb'

print(re.fullmatch(pattern, 'aaaabbb'))

