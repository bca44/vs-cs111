from operator import add, mul


def product(n):
    if n < 1:
        raise ValueError
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def summation(n):
    if n < 1:
        raise ValueError
    return sum(range(1, n + 1))


def accumulate(operation, initial, n):
    if initial > n or type(initial) is not int:
        raise ValueError
    for i in range(initial + 1, n + 1):
        initial = operation(initial, i)
    return initial


def product_short(initial, n):
    return accumulate(mul, initial, n)


def summation_short(initial, n):
    return accumulate(add, initial, n)


#############################################
# Q3

def square(x):
    return x * x


def sqrt(x):
    return x ** 0.5 # x^0.5 == √x


def mean(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"
    
    total = 0
    for num in numbers:
        total += num

    return total / len(numbers)


def median(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    numbers = sorted(numbers) 
    # `sorted` returns a sorted list. `sorted` works. 
    if len(numbers) % 2 == 0:
        right_mid = len(numbers) // 2
        left_mid = right_mid - 1
        middle_list = [numbers[left_mid], numbers[right_mid]]
        return mean(middle_list)
    else:
        middle = len(numbers) // 2
        return numbers[middle]


def mode(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    counts = {}
    running_high_num = 0
    counts[running_high_num] = 0
    for num in numbers:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        
        if counts[num] > counts[running_high_num]:
            running_high_num = num

    return running_high_num


def std_dev(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    avg = mean(numbers)
    total_dist = 0
    for num in numbers:
        total_dist += square(num - avg)

    return sqrt(total_dist / len(numbers))


def stat_analysis(numbers):
    assert isinstance(numbers, list), "Must be list"
    assert len(numbers) > 0, "Must contain numbers"

    info ={
        "mean": mean(numbers),
        "median": median(numbers),
        "mode": mode(numbers),
        "std_dev": std_dev(numbers)
    }
    return info
    

#############################################
# (OPTIONAL) Write your code here for Invert and Change
if __name__ == "__main__":
    std_dev([1, 2, 3, 4, 5])
