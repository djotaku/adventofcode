from sys import path
import re
path.insert(0, '../../input_parsing')
import parse_input


def create_aunt_sue_dictionary(list_of_aunts):
    regex = re.compile(r'Sue (\d*): (\w*): (\d*), (\w*): (\d*), (\w*): (\d*)')
    aunts = {}
    for aunt in list_of_aunts:
        matches = re.findall(regex, aunt)
        aunts[matches[0][0]] = {
            matches[0][1]: int(matches[0][2]),
            matches[0][3]: int(matches[0][4]),
            matches[0][5]: int(matches[0][6]),
        }

    return aunts


def find_the_aunt(aunt_dictionary):
    potential_aunts_2 = aunt_dictionary.copy()
    for key, values in aunt_dictionary.items():
        if values.get("children") not in [3, None]:
            del potential_aunts_2[key]
        elif values.get('cats') is not None and values.get("cats") <= 7:
            del potential_aunts_2[key]
        elif values.get("samoyeds") not in [2, None]:
            del potential_aunts_2[key]
        elif values.get('pomeranians') is not None and values.get("pomeranians") >= 3:
            del potential_aunts_2[key]
        elif values.get("akitas") not in [0, None]:
            del potential_aunts_2[key]
        elif values.get("vizslas") not in [0, None]:
            del potential_aunts_2[key]
        elif values.get('goldfish') is not None and values.get("goldfish") >= 5:
            del potential_aunts_2[key]
        elif values.get('trees') is not None and values.get("trees") <= 3:
            del potential_aunts_2[key]
        elif values.get("cars") not in [2, None]:
            del potential_aunts_2[key]
        elif values.get("perfumes") not in [1, None]:
            del potential_aunts_2[key]
    return potential_aunts_2


if __name__ == "__main__":
    all_the_aunts = parse_input.input_per_line('../input.txt')
    aunt_sue_dictionary = create_aunt_sue_dictionary(all_the_aunts)
    print(f"The Aunt Sue who sent the present is {find_the_aunt(aunt_sue_dictionary)}")
