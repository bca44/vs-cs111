def largest_factor(n):
    """
    >>> largest_factor(0)
    0
    >>> largest_factor(1)
    1
    >>> largest_factor(2)
    1
    >>> largest_factor(3)
    1
    >>> largest_factor(4)
    2
    >>> largest_factor(7)
    1
    >>> largest_factor(8)
    4
    """
    if n == 0:  # better way to do this?? (i.e. without hardcoding for 0 case)
        return 0

    biggest_factor = 1
    i = 2
    while i < n:
        if n % i == 0:
            biggest_factor = i
        i += 1

    return biggest_factor


def missing_digits(n):
    """
    >>> missing_digits(33)
    0
    >>> missing_digits(1278)
    4
    >>> missing_digits(1122)
    0
    >>> missing_digits(9)
    0
    """
    for i in range(len(str(n)) - 1):  # validate input as non-decreasing
        if len(str(n)) == 1:  # if only one digit, no missing digits possible
            return 0
        elif str(n)[i] > str(n)[i + 1]:
            print("Invalid input. Must be in non-decreasing order")
            return

    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = last_digit - second_to_last_digit
        if diff > 1:
            counter += diff - 1
        n //= 10

    return counter
