"""
Q2: Write a function to find maximum element in a list/collection without max().
"""

def find_maximum(numbers):
    if not numbers:
        return None
    
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
    return current_max

if __name__ == "__main__":
    data = [12, 45, 2, 89, 34, 89, 10]
    print("Max in list:", find_maximum(data))
    print("Max in empty list:", find_maximum([]))
