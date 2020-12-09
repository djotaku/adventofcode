from collections import deque


def validate_number(list_of_numbers, number_to_check):
    for number in list_of_numbers:
        if number_to_check - number in list_of_numbers and number_to_check - number != number:
            return True
    return False


def find_weakness(input_file, preamble):
    with open(input_file, 'r') as file:
        crypto_sequence = file.readlines()
        evaluation_deque = deque(maxlen=preamble)
        for number in range(0, preamble):
            evaluation_deque.append(int(crypto_sequence[number]))
        for number in range(preamble, len(crypto_sequence)):
            found_it = validate_number(evaluation_deque, int(crypto_sequence[number]))
            if not found_it:
                print(f"Found the number that breaks the sequence: {crypto_sequence[number]}")
                return int(crypto_sequence[number])
            else:
                evaluation_deque.append(int(crypto_sequence[number]))


if __name__ == "__main__":
    find_weakness('input', 25)
