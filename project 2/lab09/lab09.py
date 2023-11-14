import random


def in_range1(input):
    """Write a function that checks to see if input is 
    within the range of 1-100 and have it return False if not
    >>> in_range1(9)
    True
    >>> in_range1(-4)
    False
    """
    if input in range(1, 100):
        return True
    return False


def in_range2(num):
    """Redo in_range1, but throw an exception instead of 
    throwing false
    """
    if num not in range(1, 100):
        raise ValueError


def main():
    """
    generates 1000 random numbers between 1 and 101
    calls in_range1() to validate each number
    """
    rand_list = [random.randint(1, 101) for i in range(1000)]
    [in_range1(i) for i in rand_list]

    for i in rand_list:
        try:
            in_range2(i)
        except ValueError as val:
            print(f"Number outside of specified bounds. Error type: {type(val)}")


if __name__ == "__main__":
    main()
