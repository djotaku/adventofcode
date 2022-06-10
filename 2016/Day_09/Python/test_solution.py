from . import solution


def test_decompress_string():
    assert solution.decompress_string("ADVENT") == "ADVENT"
    assert solution.decompress_string("A(1x5)BC") == "ABBBBBC"
    assert solution.decompress_string("(3x3)XYZ") == "XYZXYZXYZ"
    assert solution.decompress_string("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
    assert solution.decompress_string("(6x1)(1x3)A") == "(1x3)A"
    assert solution.decompress_string("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"


def test_decompress_version_2():
    assert solution.decompress_version_2("(3x3)XYZ") == 9
    assert solution.decompress_version_2("X(8x2)(3x3)ABCY") == 20

