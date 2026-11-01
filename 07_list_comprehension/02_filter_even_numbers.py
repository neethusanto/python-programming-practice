"""
Q2: Filter only even numbers from a given list using list comprehension with if condition.
"""

def filter_evens(numbers):
    return [x for x in numbers if x % 2 == 0]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Even numbers:", filter_evens(nums))
