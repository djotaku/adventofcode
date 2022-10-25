import solution


def test_flip_bits():
    assert solution.flip_bits('1') == '0'
    assert solution.flip_bits('00') == "11"
    assert solution.flip_bits('01') == '10'


def test_generate_checksum():
    assert solution.generate_checksum('110010110100') == "100"


def test_fill_disk():
    assert solution.fill_disk("10000", 20) == "10000011110010000111"
