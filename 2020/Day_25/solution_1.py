def find_loop_size(public_key):
    value = 1
    for number in range(1, 1000):
        value = value * 7
        value = value % 20201227
        if value == public_key:
            return number


def find_encryption_key(door_public_key, card_loop_size):
    value = 1
    for number in range(1, card_loop_size + 1):
        value = value * door_public_key
        value = value % 20201227
    return value


if __name__ == "__main__":
    door_public_key = 18356117
    card_public_key = 5909654
    card_loop_size = find_loop_size(card_public_key)
    encryption_key = find_encryption_key(door_public_key, card_loop_size)
    print(f'{encryption_key=}')
