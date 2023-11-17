from byu_pytest_utils import max_score, with_import
import ast
import inspect
import pytest


@max_score(6)
@with_import('lab13', 'multiply')
def test_multiply(multiply):
    tree = ast.parse(inspect.getsource(multiply))
    recursive_call_seen = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Mult):
            pytest.fail(
                'You may not use the * operator in the multiply function')
        elif isinstance(node, ast.Call) and node.func.id == 'multiply':
            recursive_call_seen = True
    if not recursive_call_seen:
        pytest.fail(
            'In the multiply function, you must make a recursive call to the multiply function')

    assert multiply(0, 0) == 0
    assert multiply(0, 3) == 0
    assert multiply(0, 4) == 0
    assert multiply(2, 0) == 0
    assert multiply(5, 0) == 0
    assert multiply(3, 1) == 3
    assert multiply(1, 7) == 7
    assert multiply(5, 3) == 15
    assert multiply(4, 7) == 28
    assert multiply(13, 12) == 156


@max_score(7)
@with_import('lab13', 'is_prime')
def test_is_prime(is_prime):
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert is_prime(13)
    assert not is_prime(16)
    assert is_prime(31)
    assert not is_prime(35)


@max_score(7)
@with_import('lab13', 'skip_mul')
def test_skip_mul(skip_mul):
    tree = ast.parse(inspect.getsource(skip_mul))
    recursive_call_seen = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and node.func.id == 'skip_mul':
            recursive_call_seen = True
    if not recursive_call_seen:
        pytest.fail(
            'In the skip_mul function, you must make a recursive call to the skip_mul function')

    assert skip_mul(1) == 1
    assert skip_mul(2) == 2
    assert skip_mul(5) == 15
    assert skip_mul(6) == 48
    assert skip_mul(8) == 384
