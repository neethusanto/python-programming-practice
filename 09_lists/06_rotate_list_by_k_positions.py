"""
Q6: Rotate a list right by K positions without slice shortcuts or deque.rotate().
"""

def rotate_right(items, k):
    n = len(items)
    if n == 0:
        return items
    k = k % n
    result = [None] * n
    for i in range(n):
        new_pos = (i + k) % n
        result[new_pos] = items[i]
    return result

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print("Rotated right by 3:", rotate_right(nums, 3))
