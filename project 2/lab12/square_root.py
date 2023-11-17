def square_root(num):
    """Calculate the square root with 0.000001 precision"""
    num = abs(num)

    low = 0
    high = num
    middle = num
    old_middle = -1
    iteration_count = 0

    accuracy = 0.000001
    while abs(old_middle - middle) > accuracy:
        old_middle = middle

        middle = (high + low) / 2
        middle_squared = middle ** 2

        if middle_squared > num:
            high = middle
        else:
            low = middle

        iteration_count += 1

    return round(middle, 4), iteration_count


# Testing code
print(square_root(9))
