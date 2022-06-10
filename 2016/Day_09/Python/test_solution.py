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
    assert solution.decompress_version_2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    assert solution.decompress_version_2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445

