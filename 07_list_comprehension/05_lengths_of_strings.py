"""
Q5: Find length of each string in a list using list comprehension without len().
"""

def str_len(s):
    count = 0
    for _ in s:
        count += 1
    return count

def string_lengths(words):
    return [str_len(w) for w in words]

if __name__ == "__main__":
    sample = ["apple", "banana", "kiwi", "watermelon"]
    print("Word lengths:", string_lengths(sample))
