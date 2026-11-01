"""
Q5: Count frequency of words in a sentence using a dictionary without Counter or count().
"""

def word_frequencies(sentence):
    # Split manually by space
    words = []
    current = ""
    for ch in sentence:
        if ch == ' ':
            if current:
                words.append(current)
                current = ""
        else:
            current += ch
    if current:
        words.append(current)
        
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

if __name__ == "__main__":
    text = "apple banana apple cherry banana apple"
    print("Word frequencies:", word_frequencies(text))
