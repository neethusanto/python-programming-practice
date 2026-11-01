"""
Q5: Use a lambda function with filter() to filter even numbers from a list.
"""

def get_evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Filtered evens:", get_evens(data))
