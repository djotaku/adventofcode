from . import part_2


def test_all_prime_factors():
    assert part_2.all_factors(2) == [1, 2]
    assert part_2.all_factors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]


def test_presents_per_house():
    # first let's test some base cases where we know an elf hasn't reached 50 houses
    assert part_2.presents_per_house([1]) == 11
    assert part_2.presents_per_house([1, 2]) == 33
    assert part_2.presents_per_house([1, 51]) == 561


#def test_problem_input():
#    house_2_prime_factors = part_1.prime_factors(2)
#    house_2_presents = part_1.sum_of_divisors(house_2_prime_factors) * 10
#   assert house_2_presents == 30
#    house_3_prime_factors = part_1.prime_factors(3)
#    house_3_presents = part_1.sum_of_divisors(house_3_prime_factors) * 10
#    assert house_3_presents == 40
#    house_9_prime_factors = part_1.prime_factors(9)
#    house_9_presents = part_1.sum_of_divisors(house_9_prime_factors) * 10
#    assert house_9_presents == 130
