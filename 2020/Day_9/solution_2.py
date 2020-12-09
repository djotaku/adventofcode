from collections import deque


def find_the_sum(input_list, summation_number):
    evaluation_deque = deque(input_list)
    sum = 0
    summation_queue = []
    for number in range(0, len(evaluation_deque)):
        summation_queue.append(evaluation_deque[number])
        sum += evaluation_deque[number]
        if sum == summation_number:
            return summation_queue
    evaluation_deque.popleft()
    return find_the_sum(evaluation_deque, summation_number)


def find_weakness(input_list):
    sorted_list = sorted(input_list)
    return sorted_list[0] + sorted_list[-1]


def final_answer(input_file, bad_number):
    with open(input_file, 'r') as file:
        crypto_list = [int(line) for line in file.readlines()]
        summation_list = find_the_sum(crypto_list, bad_number)
    return find_weakness(summation_list)


if __name__ == "__main__":
    print(final_answer('input', 23278925))
