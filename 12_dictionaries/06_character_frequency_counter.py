"""
Q6: Count frequency of each character in a string using a dictionary without built-ins.
"""

def char_frequencies(text):
    freq = {}
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

if __name__ == "__main__":
    sample = "programming"
    print("Character frequencies:", char_frequencies(sample))
