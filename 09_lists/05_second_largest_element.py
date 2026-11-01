"""
Q5: Find the second largest distinct number in a list without using sort().
"""

def second_largest(items):
    first = None
    second = None
    for x in items:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 35, 34]
    print("Second largest:", second_largest(arr))
