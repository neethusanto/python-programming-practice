"""
Q15: Remove all vowels from a string using list comprehension and join.
"""

def remove_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return "".join([ch for ch in text if ch not in vowels])

if __name__ == "__main__":
    sentence = "Beautiful Python List Comprehension"
    print("Without vowels:", remove_vowels(sentence))
