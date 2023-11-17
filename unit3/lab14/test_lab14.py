from byu_pytest_utils import max_score, with_import
import inspect
import pytest
import re


def link_eq(Link, left, right):
    if left is not Link.empty and not isinstance(left, Link):
        return False
    if right is not Link.empty and not isinstance(right, Link):
        return False
    while left is not Link.empty and right is not Link.empty:
        if left.first != right.first:
            return False
        left = left.rest
        right = right.rest
    if left is not Link.empty or right is not Link.empty:
        return False
    return True


@max_score(5)
@with_import('lab14', 'convert_link')
@with_import('lab14', 'Link')
def test_convert_link(Link, convert_link, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    key = []
    input = Link.empty
    output = convert_link(input)
    assert output == key

    key = [1, 2, 3, 4]
    input = Link(1, Link(2, Link(3, Link(4))))
    output = convert_link(input)
    assert output == key

    key = ['C', 'S', 1, 1, 1]
    input = Link('C', Link('S', Link(1, Link(1, Link(1)))))
    output = convert_link(input)
    assert output == key


@max_score(5)
@with_import('lab14', 'store_digits')
@with_import('lab14', 'Link')
def test_store_digits(Link, store_digits, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    cleaned = re.sub(
        r'#.*?\n|""".*?"""', '', inspect.getsource(store_digits), flags=re.DOTALL)
    for forbidden in 'str', 'reversed':
        if forbidden in cleaned:
            pytest.fail(f'You may not use {forbidden} in store_digits')

    key = Link(1)
    output = store_digits(1)
    assert output == key

    key = Link(2, Link(3, Link(4, Link(5))))
    output = store_digits(2345)
    assert output == key

    key = Link(8, Link(7, Link(6)))
    output = store_digits(876)
    assert output == key


@max_score(5)
@with_import('lab14', 'every_other')
@with_import('lab14', 'Link')
def test_every_other(Link, every_other, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    key = Link.empty
    link = Link.empty
    every_other(link)
    assert link == key

    key = Link(1)
    link = Link(1)
    every_other(link)
    assert link == key

    key = Link(1, Link(3))
    link = Link(1, Link(2, Link(3, Link(4))))
    every_other(link)
    assert link == key

    key = Link(1, Link(3, Link(5, Link(7))))
    link = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7)))))))
    every_other(link)
    assert link == key


@max_score(5)
@with_import('lab14', 'deep_map_mut')
@with_import('lab14', 'Link')
def test_deep_map_mut(Link, deep_map_mut, monkeypatch):
    monkeypatch.setattr(Link, '__eq__', lambda self,
                        other: link_eq(Link, self, other))

    def patched_init(self, first, rest=Link.empty):
        pytest.fail(
            'You may not create any new Link objects, only mutate the existing ones')

    def double(x):
        return x * 2

    key = Link.empty
    link = Link.empty
    with monkeypatch.context() as m:
        m.setattr(Link, '__init__', patched_init)
        deep_map_mut(double, link)
    assert link == key

    key = Link(2, Link(Link(4, Link(6, Link(Link(8, Link(10))))), Link(12)))
    link = Link(1, Link(Link(2, Link(3, Link(Link(4, Link(5))))), Link(6)))
    with monkeypatch.context() as m:
        m.setattr(Link, '__init__', patched_init)
        deep_map_mut(double, link)
    assert link == key
