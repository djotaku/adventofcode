from . import part_1


def test_generate_replacements():
    replacements = part_1.generate_replacements("H", "HO", "HOH")
    assert replacements == ["HOOH", "HOHO"]
    replacements = part_1.generate_replacements("H", "OH", "HOH")
    assert replacements == ["OHOH", "HOOH"]
    replacements = part_1.generate_replacements("O", "HH", "HOH")
    assert replacements == ["HHHH"]


def test_generate_molecule_dictionary():
    list_of_molecules = ["Al => ThF", "Al => ThRnFAr"]
    assert part_1.generate_molecule_tuple(list_of_molecules) == [("Al", "ThF"), ("Al", "ThRnFAr")]
