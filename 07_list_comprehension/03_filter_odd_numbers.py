"""
Q3: Filter only odd numbers from a list using list comprehension.
"""

def filter_odds(numbers):
    return [x for x in numbers if x % 2 != 0]

if __name__ == "__main__":
    nums = [11, 22, 33, 44, 55, 66]
    print("Odd numbers:", filter_odds(nums))
