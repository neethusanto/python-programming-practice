"""
Q8: Remove an element from a set if present without discard() or remove().
"""

def remove_from_set(s, target):
    new_s = set()
    for x in s:
        if x != target:
            new_s.add(x)
    return new_s

if __name__ == "__main__":
    s = {10, 20, 30, 40}
    print("After removing 20:", remove_from_set(s, 20))
