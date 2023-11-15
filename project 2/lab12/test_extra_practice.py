from byu_pytest_utils import with_import


@with_import('extra_practice', 'largest_factor')
def test_largest_factor(largest_factor):
    assert largest_factor(0) == 0
    assert largest_factor(2) == 1
    assert largest_factor(1) == 1
    assert largest_factor(3) == 1
    assert largest_factor(4) == 2
    assert largest_factor(8) == 4
    assert largest_factor(7) == 1
    assert largest_factor(9) == 3
    assert largest_factor(16) == 8
    assert largest_factor(25) == 5


@with_import('extra_practice', 'missing_digits')
def test_missing_digits(missing_digits):
    assert missing_digits(33) == 0
    assert missing_digits(1278) == 4
    assert missing_digits(1122) == 0
    assert missing_digits(9) == 0
