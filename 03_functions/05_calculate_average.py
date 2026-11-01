"""
Q5: Write a function to calculate the mean/average of numbers without sum() or len().
"""

def calculate_average(items):
    total = 0
    count = 0
    for item in items:
        total += item
        count += 1
    
    if count == 0:
        return 0.0
    return total / count

if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    print("Average:", calculate_average(nums))
