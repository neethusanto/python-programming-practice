"""
Q12: Write a function to count occurrences of a specific element without list.count().
"""

def count_frequency(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

if __name__ == "__main__":
    data = [1, 2, 2, 3, 2, 4, 2, 5]
    print("Count of 2:", count_frequency(data, 2))
    print("Count of 9:", count_frequency(data, 9))
