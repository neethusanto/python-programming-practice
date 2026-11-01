"""
Q3: Count occurrences of an element in a tuple without using tuple.count().
"""

def count_in_tuple(tup, target):
    count = 0
    for x in tup:
        if x == target:
            count += 1
    return count

if __name__ == "__main__":
    t = (1, 2, 3, 2, 4, 2, 5)
    print("Occurrences of 2:", count_in_tuple(t, 2))
