from byu_pytest_utils import max_score, with_import

@max_score(10)
@with_import('digit_counter', 'digit_counter')
def test_digit_counter(digit_counter):
    def is_even(x):
        return x % 2 == 0

    def is_odd(x):
        return x % 2 == 1

    assert digit_counter(is_even, 1112) == 1
    assert digit_counter(is_even, 1832233) == 3
    assert digit_counter(is_odd, 134) == 2
