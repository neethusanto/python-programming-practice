"""
Q3: Reverse a list in-place using two pointers without list.reverse() or [::-1].
"""

def reverse_list(items):
    left = 0
    right = len(items) - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]
    print("Reversed:", reverse_list(data))
