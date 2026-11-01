"""
Q6: Use a lambda function with map() to calculate cubes of all numbers in a list.
"""

def get_cubes(nums):
    return list(map(lambda x: x * x * x, nums))

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    print("Cubes:", get_cubes(data))
