from . import part_2


def test_string_code_length():
    assert part_2.string_code_length(r'""') == 2
    assert part_2.string_code_length(r'"abc"') == 5
    assert part_2.string_code_length(r'"aaa\"aaa"') == 10
    assert part_2.string_code_length(r'"\x27"') == 6
    assert part_2.string_code_length(r'"\xff\xca"') == 10


def test_encoded_strings():
    assert part_2.encoded_strings(r'""') == 6
    assert part_2.encoded_strings(r'"abc"') == 9
