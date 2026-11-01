"""
Q13: Write a function to find the second largest number in a list without sort() or max().
"""

def find_second_largest(items):
    first = None
    second = None
    
    for x in items:
        if first is None or x > first:
            second = first
            first = x
        elif x != first:
            if second is None or x > second:
                second = x
                
    return second

if __name__ == "__main__":
    nums = [10, 20, 4, 45, 99, 99, 32]
    print("Second largest:", find_second_largest(nums))
