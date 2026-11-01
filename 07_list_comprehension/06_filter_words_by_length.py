"""
Q6: Filter words whose length is greater than a threshold K using list comprehension.
"""

def str_len(s):
    c = 0
    for _ in s:
        c += 1
    return c

def filter_by_length(words, min_len):
    return [w for w in words if str_len(w) > min_len]

if __name__ == "__main__":
    words = ["cat", "elephant", "dog", "tiger", "hippopotamus", "ox"]
    print("Words with length > 4:", filter_by_length(words, 4))
