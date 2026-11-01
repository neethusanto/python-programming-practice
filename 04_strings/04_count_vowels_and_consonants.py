"""
Q4: Count total vowels and consonants in a string without count(), lower(), or upper().
"""

def count_vowels_consonants(s):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    v_count = 0
    c_count = 0
    
    for ch in s:
        if ch in vowels:
            v_count += 1
        elif ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            c_count += 1
            
    return v_count, c_count

if __name__ == "__main__":
    text = "Hello World 2026!"
    v, c = count_vowels_consonants(text)
    print(f"Text: '{text}' -> Vowels: {v}, Consonants: {c}")
