"""
Q12: Create a set from a list of duplicated items by manually adding elements.
"""

def list_to_set_dedup(items):
    unique_set = set()
    for item in items:
        unique_set.add(item)
    return unique_set

if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 4, 4, 5]
    print("Set from list:", list_to_set_dedup(nums))
