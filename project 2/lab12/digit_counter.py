def digit_counter(func, num):
    """Return the number of digits when func(num) is true"""
    counter = 0

    while num >= 0:
        if func(num % 10):
            counter += 1
            num = num // 10

    return counter


# Function to test with
def is_even(x):
    return x % 2 == 0


"""ADD_TESTING_CODE"""
