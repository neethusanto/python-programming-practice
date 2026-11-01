"""
Q4: Remove duplicates from a list while maintaining element insertion order without set().
"""

def remove_duplicates(items):
    unique = []
    for x in items:
        found = False
        for u in unique:
            if u == x:
                found = True
                break
        if not found:
            unique.append(x)
    return unique

if __name__ == "__main__":
    nums = [10, 20, 30, 20, 40, 10, 50, 30]
    print("Deduplicated:", remove_duplicates(nums))
