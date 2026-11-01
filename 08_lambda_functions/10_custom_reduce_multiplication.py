"""
Q10: Calculate cumulative product of list elements using a lambda accumulator.
"""

def custom_reduce(func, iterable, initial=None):
    it = iter(iterable)
    if initial is None:
        value = next(it)
    else:
        value = initial
    for element in it:
        value = func(value, element)
    return value

if __name__ == "__main__":
    multiply = lambda a, b: a * b
    nums = [1, 2, 3, 4, 5]
    print("Product of list:", custom_reduce(multiply, nums))
