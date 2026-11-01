"""
Q3: Write a function to find minimum element in a list without min().
"""

def find_minimum(numbers):
    if not numbers:
        return None
    
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == "__main__":
    data = [45, 12, 99, 3, -15, 20]
    print("Min in list:", find_minimum(data))
