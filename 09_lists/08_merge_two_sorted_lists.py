"""
Q8: Merge two already sorted lists into a single sorted list in O(n + m) time without sort().
"""

def merge_sorted(l1, l2):
    merged = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    while i < len(l1):
        merged.append(l1[i])
        i += 1
    while j < len(l2):
        merged.append(l2[j])
        j += 1
    return merged

if __name__ == "__main__":
    a = [2, 5, 8, 12]
    b = [1, 3, 7, 9, 15]
    print("Merged:", merge_sorted(a, b))
