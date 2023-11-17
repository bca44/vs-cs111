def filter(lst, cond):
    """Returns a list where each element is an element where `cond(elem)` returns `True`.

    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> is_even = lambda x : x % 2 == 0 # Even numbers have remainder 0 when divided by 2.
    >>> filter(nums, is_even)
    [2, 4, 6, 8, 10]
    """
    return [element for element in lst if cond(element)]


def print_cond(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> print_cond(5)(is_even)
    2
    4
    """
    return lambda cond: print("\n".join(str(i) for i in range(1, n + 1) if cond(i)))


def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6
    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    return lambda n: len([number for number in range(1, n + 1) if condition(n, number)])


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    count = [0]

    def inner_print(x):
        if count[0] >= n:
            print("done")
        else:
            print(x)
            count[0] += 1
        return inner_print
    return inner_print


# OPTIONAL QUESTION
#####################
def increment(n):
    return n + 1


def square(n):
    return n*n


def triple(n):
    return n*3


def make_repeater(func, n):
    """Return the function that computes the nth application of func.
    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def function(operand):
        for i in range(n):
            operand = func(operand)
        return operand

    return function


def main():
    pass


if __name__ == "__main__":
    main()
