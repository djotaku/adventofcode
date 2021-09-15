from collections import Counter
import math
from sys import path
path.insert(0, '../../input_parsing')
import parse_input


def prime_factors(number_to_factorize):
    """Return a list with the prime factors of the given number."""

    prime_factor_list = []

    # Print the number of two's that divide our given number
    while number_to_factorize % 2 == 0:
        prime_factor_list.append(2)
        number_to_factorize = number_to_factorize / 2

    # given number must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(number_to_factorize)) + 1, 2):

        # while i divides given number , print i and divide given number
        while number_to_factorize % i == 0:
            prime_factor_list.append(i)
            number_to_factorize = number_to_factorize / i

    # Condition if n is a prime number greater than 2
    if number_to_factorize > 2:
        prime_factor_list.append(number_to_factorize)

    return prime_factor_list


def sum_of_divisors(list_of_prime_factors):
    """Take a list of prime factors and figure out the sum of divisors.

    Formula is σ(p**a) = (p**(a+1) − 1)/(p − 1) .
    """
    numbers_and_exponents = Counter(list_of_prime_factors)
    formula_results = [(factor**(exponent+1) - 1) / (factor - 1)
                       for factor, exponent in numbers_and_exponents.items()]

    return math.prod(formula_results)


if __name__ == "__main__":
    house_number = 2
    PUZZLE_INPUT = 34000000
    presents_delivered = 0
    while presents_delivered < 34000000:
        # print(house_number)
        presents_delivered = sum_of_divisors(prime_factors(house_number)) * 10
        # print(f"{presents_delivered=}")
        house_number += 1
    print(f"The lowest house number is {house_number-1}")

# 786241 is too high
