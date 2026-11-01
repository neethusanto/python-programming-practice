"""
Q10: Write a function to reverse a list in-place without list.reverse() or [::-1].
"""

def reverse_list(items):
    n = 0
    for _ in items:
        n += 1
        
    left = 0
    right = n - 1
    while left < right:
        items[left], items[right] = items[right], items[left]
        left += 1
        right -= 1
    return items

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print("Reversed:", reverse_list(nums))
