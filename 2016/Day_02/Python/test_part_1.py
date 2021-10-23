from . import part_1


def test_figure_out_button():
    assert part_1.figure_out_button(1, 1, ["U"]) == (2, 0, 1)
    assert part_1.figure_out_button(1, 1, ["U", "U"]) == (2, 0, 1)
