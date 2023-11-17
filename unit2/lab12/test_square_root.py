from byu_pytest_utils import max_score, with_import


@max_score(10)
@with_import('square_root', 'square_root')
def test_square_root(square_root):
    result, iterations = square_root(9)
    assert result == 3.0000
    assert iterations <= 24

    result, iterations = square_root(16)
    assert result == 4.0000
    assert iterations <= 24

    result, iterations = square_root(10)
    assert result == 3.1623
    assert iterations <= 24

    result, iterations = square_root(3)
    assert result == 1.7321
    assert iterations <= 22
