def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:  # first base case
        return 2
    elif n == 1:  # second base case
        return 1
    else:
        return n * skip_mul(n - 2)  # recursive call


def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    m = m + m(n-1) = m + m + m(n-2) = m + m + m + m(n-3) = ... = m + m + ... + m
    >>> multiply(5, 3)
    15
    >>> multiply(4, 7)
    28
    >>> multiply(13, 12)
    156
    """
    if n == 1:
        return m # base case
    else:
        return m + multiply(m, n - 1)  # recursive call


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(n, i):
        if i == 1:  # True base case
            return True
        elif n % i == 0:  # False base case
            return False
        else:  # recursive call
            return helper(n, i - 1)
    return helper(n, n - 1)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    count = 0

    def hail_helper(n, count):
        if n == 1:  # base/termination case
            print(n)
            return count + 1
        elif n % 2 == 0:  # even case
            print(n)
            count += 1
            return hail_helper(n // 2, count)
        else:  # odd case
            print(n)
            count += 1
            return hail_helper(3 * n + 1, count)
    return hail_helper(n, count)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    def path_helper(m, n):
        if m == 1 or n == 1:
            return 1
        else:
            return path_helper(m - 1, n) + path_helper(m, n - 1)
    return path_helper(m, n)
