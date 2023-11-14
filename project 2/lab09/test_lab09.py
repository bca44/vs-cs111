from byu_pytest_utils import max_score, with_import
import pytest


@max_score(2)
@with_import('lab09', 'in_range1')
def test_in_range1(in_range1):
    assert in_range1(9)
    assert not in_range1(-4)


@max_score(8)
@with_import('lab09', 'in_range2')
def test_in_range2(in_range2):
    in_range2(9)

    with pytest.raises(Exception):
        in_range2(-4)
        pytest.fail("in_range2(-4) didn't raise an exception")


@max_score(10)
@with_import('Grid', 'Grid')
def test_grid_get_and_set_out_of_bounds(Grid):
    grid = Grid(3, 3)
    for y in range(3):
        for x in range(3):
            grid.get(x, y)
            grid.set(x, y, None)

    for y in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(-1, y)
            pytest.fail(f"{grid}.get(-1, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(-1, y, None)
            pytest.fail(f"{grid}.set(-1, {y}, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(3, y)
            pytest.fail(f"{grid}.get(3, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(3, y, None)
            pytest.fail(f"{grid}.set(3, {y}, None) didn't raise an exception")

    for x in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(x, -1)
            pytest.fail(f"{grid}.get({x}, -1) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, -1, None)
            pytest.fail(f"{grid}.set({x}, -1, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(x, 3)
            pytest.fail(f"{grid}.get({x}, 3) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, 3, None)
            pytest.fail(f"{grid}.set({x}, 3, None) didn't raise an exception")
