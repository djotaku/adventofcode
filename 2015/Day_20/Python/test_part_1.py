from . import part_1


def test_prime_factors():
    assert part_1.prime_factors(2) == [2]
    assert part_1.prime_factors(3) == [3]
    assert part_1.prime_factors(4) == [2, 2]
    assert part_1.prime_factors(315) == [3, 3, 5, 7]


def test_sum_of_divisors():
    factors = [2, 2, 2, 3, 3]
    assert part_1.sum_of_divisors(factors) == 195


def test_problem_input():
    house_2_prime_factors = part_1.prime_factors(2)
    house_2_presents = part_1.sum_of_divisors(house_2_prime_factors) * 10
    assert house_2_presents == 30
    house_3_prime_factors = part_1.prime_factors(3)
    house_3_presents = part_1.sum_of_divisors(house_3_prime_factors) * 10
    assert house_3_presents == 40
    house_9_prime_factors = part_1.prime_factors(9)
    house_9_presents = part_1.sum_of_divisors(house_9_prime_factors) * 10
    assert house_9_presents == 130
