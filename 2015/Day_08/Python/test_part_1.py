from . import part_1


def test_string_code_length():
    assert part_1.string_code_length(r'""') == 2
    assert part_1.string_code_length(r'"abc"') == 5
    assert part_1.string_code_length(r'"aaa\"aaa"') == 10
    assert part_1.string_code_length(r'"\x27"') == 6
    assert part_1.string_code_length(r'"\xff\xca"') == 10


def test_in_memory_strings():
    assert part_1.in_memory_strings(r'""') == 0
    assert part_1.in_memory_strings(r'"abc"') == 3
    assert part_1.in_memory_strings(r'"aaa\"aaa"') == 7
    assert part_1.in_memory_strings(r'"\x27"') == 1
    assert part_1.in_memory_strings(r'"\xff"') == 1
    assert part_1.in_memory_strings(r'"\xff\xca"') == 2
    assert part_1.in_memory_strings(r'"\\\\"') == 2
    assert part_1.in_memory_strings(r'"jcrkptrsasjp\\\"cwigzynjgspxxv\\vyb"') == 32
    assert part_1.in_memory_strings(r'"oh\\x\\h"') == 6
    assert part_1.in_memory_strings(r'"\xzz\xll"') == 8
    assert part_1.in_memory_strings(r'"\\\"') == 2
    assert part_1.in_memory_strings(r'"\\\""') == 2
    assert part_1.in_memory_strings(r'"\\\xff\xca"') == 3
    assert part_1.in_memory_strings(r'"\xzz\xzz"') == 8
    assert part_1.in_memory_strings(r'"\\\"') == 2
    assert part_1.in_memory_strings(r'"\\\\\\"') == 3
    assert part_1.in_memory_strings(r'"\\\\\\\"') == 4
    assert part_1.in_memory_strings(r'"\"\""') == 2
    assert part_1.in_memory_strings(r'"\\"\""') == 3
    assert part_1.in_memory_strings(r'"\x\\"') == 3
    assert part_1.in_memory_strings(r'"\x3\\"') == 4
    assert part_1.in_memory_strings(r'"\x34\\"') == 2
    assert part_1.in_memory_strings(r'"\\x34\\"') == 5
