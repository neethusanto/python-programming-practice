"""
Q4: Write a function to calculate the sum of numbers in a collection without sum().
"""

def calculate_sum(items):
    total = 0
    for item in items:
        total += item
    return total

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print("Sum of items:", calculate_sum(nums))
