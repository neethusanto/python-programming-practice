"""
Q8: Count frequency of each character in a string without collections.Counter or str.count().
"""

def character_frequency(s):
    unique_chars = []
    frequencies = []
    
    for ch in s:
        found = False
        i = 0
        while i < len(unique_chars):
            if unique_chars[i] == ch:
                frequencies[i] += 1
                found = True
                break
            i += 1
        if not found:
            unique_chars.append(ch)
            frequencies.append(1)
            
    # Pair results
    result = []
    i = 0
    while i < len(unique_chars):
        result.append((unique_chars[i], frequencies[i]))
        i += 1
    return result

if __name__ == "__main__":
    sample = "programming"
    for char, count in character_frequency(sample):
        print(f"'{char}': {count}")
