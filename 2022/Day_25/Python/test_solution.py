from . import solution

def test_snafu_to_decimal():
    snafu = ['1']
    assert  solution.snafu_to_decimal(snafu) == 1
    snafu = ['1','=']
    assert solution.snafu_to_decimal(snafu) == 3
    snafu = ['1', '1', '2', '1', '-', '1', '1', '1', '0', '-', '1', '=', '0']
    assert solution.snafu_to_decimal(snafu) == 314159265

def test_decimal_to_snafu():
    decimal_number = 1
    assert solution.decimal_to_snafu(decimal_number) == '1'
    decimal_number = 3
    assert solution.decimal_to_snafu(decimal_number) == '1='
    decimal_number = 4
    assert solution.decimal_to_snafu(decimal_number) == '1-'
    decimal_number = 9
    assert solution.decimal_to_snafu(decimal_number) == '2-'
