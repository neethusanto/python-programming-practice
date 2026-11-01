"""
Q10: Count number of elements in a set without len().
"""

def set_size(s):
    count = 0
    for _ in s:
        count += 1
    return count

if __name__ == "__main__":
    s = {"apple", "banana", "cherry", "orange"}
    print("Size of set:", set_size(s))
