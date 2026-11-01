"""
Q9: Replace numbers with 'Even' or 'Odd' labels using if-else inside list comprehension.
"""

def label_even_odd(numbers):
    return ["Even" if x % 2 == 0 else "Odd" for x in numbers]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    print("Labeled:", label_even_odd(nums))
