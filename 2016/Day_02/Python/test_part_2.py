from . import part_2


def test_figure_out_button():
    assert part_2.figure_out_button(2, 0, ["U"]) == (5, 2, 0)
    assert part_2.figure_out_button(2, 0, ["D"]) == (5, 2, 0)
    assert part_2.figure_out_button(2, 0, ["L"]) == (5, 2, 0)
    assert part_2.figure_out_button(2, 0, ["R"]) == (6, 2, 1)
    assert part_2.figure_out_button(0, 0, ["L"]) == (1, 0, 0)
    assert part_2.figure_out_button(0, 0, ["R"]) == (1, 0, 0)
    assert part_2.figure_out_button(0, 0, ["U"]) == (1, 0, 0)
    assert part_2.figure_out_button(0, 0, ["D"]) == (3, 1, 1)
    assert part_2.figure_out_button(1, 1, ["U"]) == (1, 0, 0)