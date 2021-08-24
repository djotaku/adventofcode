from . import solution_1


def test_instruction_parsing():
    assert solution_1.instruction_parsing('nop +0') == ["nop", "+0"]


def test_evaluate_command():
    assert solution_1.evaluate_command(['nop', '+0']) == (1, 0)
    assert solution_1.evaluate_command(['acc', '+1']) == (1, 1)
    assert solution_1.evaluate_command(['acc', '-1']) == (1, -1)
    assert solution_1.evaluate_command(['jmp', '+1']) == (1, 0)
