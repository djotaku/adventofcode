import solution


def test_flip_bits():
    assert solution.flip_bits('1') == '0'
    assert solution.flip_bits('00') == "11"
    assert solution.flip_bits('01') == '10'
