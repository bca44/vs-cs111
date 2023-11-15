def largest_factor(n):
    biggest_factor = 1
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            biggest_factor = i
        i += 1

    return biggest_factor


def missing_digits(n):
    counter = 0
    while n > 10:
        last_digit = n % 10
        second_to_last_digit = (n // 10) % 10
        diff = last_digit - second_to_last_digit
        counter += diff
        n //= 10

    return counter