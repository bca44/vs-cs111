def digit_counter(func, num):
    """
    Returns a count of the number of digits in num for which func returns True.
    """
    counter = 0
    while num > 0:
        if func(num % 10):
            counter += 1
        num = num // 10
    return counter


def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    print(digit_counter(is_even, 123456))
