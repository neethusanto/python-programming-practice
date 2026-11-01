"""
Q14: Filter all words starting with a vowel from a list of words.
"""

def filter_vowel_starters(words):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return [w for w in words if w and w[0] in vowels]

if __name__ == "__main__":
    words = ["apple", "banana", "orange", "grape", "umbrella", "ice"]
    print("Vowel starter words:", filter_vowel_starters(words))
