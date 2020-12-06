def grouping(list_of_groups):
    grouped_list = []
    sub_list = []
    for item in list_of_groups:
        if item != "\n":
            sub_list.append(item)
        if item == '\n':
            grouped_list.append(sub_list.copy())
            sub_list.clear()
    grouped_list.append([list_of_groups[-1]])
    return grouped_list


def create_chars(string):
    a_list = []
    for char in string:
        if char != '\n':
            a_list.append(char)
    return a_list


def yes_count(list_of_entries):
    if len(list_of_entries) == 1:
        return len(create_chars(list_of_entries[0]))
    else:
        set_of_entries = set()
        temp_set_of_entries = set()
        count = 0
        for item in list_of_entries:
            characters = create_chars(item)
            for character in characters:
                temp_set_of_entries.add(character)
            if count == 0:
                set_of_entries = temp_set_of_entries.copy()
                temp_set_of_entries.clear()
                count += 1
            else:
                set_of_entries = set_of_entries & temp_set_of_entries
                count += 1
        return len(set_of_entries)


def sum_of_counts(list_of_counts):
    return sum(list_of_counts)


if __name__ == "__main__":
    with open('input', 'r') as file:
        group_list = file.readlines()
        print(sum([yes_count(group) for group in grouping(group_list)]))
