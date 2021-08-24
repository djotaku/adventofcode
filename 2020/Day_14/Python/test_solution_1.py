from . import solution_1


#def test_parse_input():
#    assert solution_1.parse_input('ref_input') == [['XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', (8, 11), (7, 101), (8, 0)]]


def test_mask_application():
    assert solution_1.mask_application('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11) == 73
    assert solution_1.mask_application('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101) == 101
    assert solution_1.mask_application('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 0) == 64
    assert solution_1.mask_application('XX001001X10X110X0001111001110X110101', 4436) == 2495735669
    assert solution_1.mask_application('XX001001X10X110X0001111001110X110101', 14455) == 2495735669


def test_sum_it():
    assert solution_1.sum_it(solution_1.parse_input('ref_input')) == 165