import solution


def test_find_capsule_time():
    discs = [(5, 4), (2, 1)]
    assert solution.find_capsule_time(discs) == 5


def test_extra_data():
    test_sentences = [
        "Disc #1 has 5 positions: at time=0, it is at position 4.",
        "Disc #1 has 2 positions: at time=0, it is at position 1."
    ]
    extracted_data = solution.extract_data(test_sentences)
    assert extracted_data == [(5, 4), (2, 1)]
