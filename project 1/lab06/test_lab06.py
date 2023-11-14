from byu_pytest_utils import max_score, with_import


@max_score(3)
@with_import('lab06', 'print_cond')
def test_print_cond_1(print_cond, capsys):
    def is_even(x):
        return x % 2 == 0
    print_cond(10)(is_even)
    cap = capsys.readouterr()
    assert cap.out == """2
4
6
8
10
"""


@max_score(4)
@with_import('lab06', 'print_cond')
def test_print_cond_2(print_cond, capsys):
    def is_multiple_of_3(x):
        return x % 3 == 0
    print_cond(11)(is_multiple_of_3)
    cap = capsys.readouterr()
    assert cap.out == """3
6
9
"""


@max_score(3)
@with_import('lab06', 'print_n')
def test_print_n_1(print_n, capsys):
    f = print_n(3)
    f(1)(2)(3)(4)(5)
    cap = capsys.readouterr()
    assert cap.out == """1
2
3
done
done
"""


@max_score(3)
@with_import('lab06', 'print_n')
def test_print_n_2(print_n, capsys):
    f = print_n(5)
    f('a')('b')('c')('d')('e')('f')
    cap = capsys.readouterr()
    assert cap.out == """a
b
c
d
e
done
"""


@max_score(3)
@with_import('lab06', 'count_cond')
def test_count_cond_1(count_cond):
    count_factors = count_cond(lambda n, i: n % i == 0)
    assert count_factors(2) == 2
    assert count_factors(4) == 3
    assert count_factors(12) == 6


@max_score(4)
@with_import('lab06', 'count_cond')
def test_count_cond_2(count_cond):
    count_factors = count_cond(lambda n, i: n % i == 0)

    def is_prime(_, i):
        return count_factors(i) == 2
    count_primes = count_cond(is_prime)

    assert count_primes(2) == 1
    assert count_primes(3) == 2
    assert count_primes(4) == 2
    assert count_primes(5) == 3
    assert count_primes(20) == 8
