"""
Q14: Group a list of words into anagrams using a dictionary without sort() or Counter.
"""

def get_char_signature(word):
    # Manual character frequency tuple key
    freq = [0] * 26
    for ch in word:
        if 'a' <= ch <= 'z':
            freq[ord(ch) - ord('a')] += 1
    return tuple(freq)

def group_anagrams(words):
    anagram_map = {}
    for w in words:
        sig = get_char_signature(w)
        if sig in anagram_map:
            anagram_map[sig].append(w)
        else:
            anagram_map[sig] = [w]
    return list(anagram_map.values())

if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped anagrams:", group_anagrams(words))
