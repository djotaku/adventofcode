import parse_input


def test_input_per_line_alpha():
    entries = parse_input.input_per_line("alpha_per_line_input.txt")
    assert entries[0] == "asdfasdf"
    assert entries[1] == "woeruwoer"
    assert entries[2] == "asdfasdf"
    assert entries[3] == "rufndnd dasdf"


def test_input_per_line_numeric():
    entries = parse_input.input_per_line("numeric_per_line_input.txt")
    assert entries[0] == "234234"
    assert entries[1] == "54565677"
    assert entries[2] == "23452345345456"
    assert entries[3] == "23423453454"
    assert entries[4] == "233232"


def test_input_per_line_alpha_numeric_symbols():
    entries = parse_input.input_per_line("alpha_numeric_symbols_per_line_input.txt")
    assert entries[0] == "dh#$liu\][asd"
    assert entries[1] == "lkhlh!@#*(&^@$%)<>?/\\"
