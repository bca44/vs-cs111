from Link import Link


def convert_link(l_lst):
    """Takes a linked list and returns a Python list with the same elements.

    >>> l_lst1 = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(l_lst1)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    # ITERATIVE SOLUTION
    # regular_list = []
    # while link is not Link.empty:
    #     regular_list.append(link.first)
    #     link = link.rest
    # return regular_list

    # OR RECURSIVE SOLUTION
    if l_lst is Link.empty:
        return []
    else:
        return [l_lst.first] + convert_link(l_lst.rest)


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> store_digits(1)
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    def digit_helper(number, divisor):
        if divisor == 1:
            return Link(number)
        else:
            leading_digit = number // divisor
            remainder = number % divisor
            return Link(leading_digit, digit_helper(remainder, divisor // 10))

    if n == 0:
        return Link(0)

    # Calculate the divisor
    divisor = 1
    while n // divisor >= 10:
        divisor *= 10

    return digit_helper(n, divisor)


def every_other(link):
    """
    Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).
    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    pass


def deep_map_mut(fn, link):
    """
    Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)
    Does not return the modified Link object.
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    pass

