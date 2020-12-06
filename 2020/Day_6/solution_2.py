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
        a_list = []
        for char in list_of_entries[0]:
            if char != '\n':
                a_list.append(char)
        return len(a_list)
    else:
        pass
    set_of_answers = set()
    for item in list_of_entries:
        for char in item:
            if char != '\n':
                set_of_answers.add(char)
    return len(set_of_answers)


def sum_of_counts(list_of_counts):
    return sum(list_of_counts)


if __name__ == "__main__":
    with open('input', 'r') as file:
        group_list = file.readlines()
        print(sum([yes_count(group) for group in grouping(group_list)]))
