import pytest
from lab11 import *


def test_product():
    assert product(1) == 1
    assert product(5) == 120
    with pytest.raises(ValueError):
        product(0)


def test_summation():
    assert summation(5) == 15
    with pytest.raises(ValueError):
        summation(0)


def test_accumulate():
    assert accumulate(add, 0, 3) == 6
    assert accumulate(add, 1, 4) == 10
    with pytest.raises(ValueError):
        accumulate(add, 1, 0)

    assert accumulate(mul, 0, 3) == 0
    assert accumulate(mul, 1, 4) == 24
    with pytest.raises(ValueError):
        accumulate(mul, 1, 0)


def test_product_short():
    assert product_short(1, 1) == 1
    assert product_short(1, 5) == 120
    with pytest.raises(ValueError):
        product_short(1, 0)


def test_summation_short():
    assert summation_short(1, 5) == 15
    with pytest.raises(ValueError):
        summation_short(1, 0)


def test_square():
    assert square(2) == 4
    assert square(9) == 81


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(16) == 4


def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert mean([0, 0, 0, 0, 2, 4]) == 1
    assert mean([5, 8]) == 6.5


def test_median():
    assert median([1, 1, 1, 4, 1, 1, 1]) == 1
    assert median([1]) == 1
    assert mean([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5.5


def test_mode():
    assert mode([1, 2, 2, 2, 3, 4, 5]) == 2
    assert mode([1, 1, 2, 2]) == 1
    assert mode([1, 1, 2, 3, 4, 5]) == 1


def test_std_dev():
    assert std_dev([1, 2, 3, 4, 5]) == pytest.approx(sqrt(2))


def test_stat_analysis():
    """Write your code here"""


# OPTIONAL
#####################################

def test_invert():
    """Write your code here"""


def test_change():
    """Write your code here"""


def test_invert_short():
    """Write your code here"""


def test_change_short():
    """Write your code here"""
