"""
Q15: Check whether two strings are anagrams of each other without using sort() or Counter.
"""

def is_anagram(str1, str2):
    # Length check
    len1 = 0
    for _ in str1:
        len1 += 1
    len2 = 0
    for _ in str2:
        len2 += 1
        
    if len1 != len2:
        return False
        
    # Count character frequencies
    char_map = {}
    for ch in str1:
        if ch in char_map:
            char_map[ch] += 1
        else:
            char_map[ch] = 1
            
    for ch in str2:
        if ch not in char_map or char_map[ch] == 0:
            return False
        char_map[ch] -= 1
        
    return True

if __name__ == "__main__":
    print("'listen' & 'silent':", is_anagram("listen", "silent"))
    print("'triangle' & 'integral':", is_anagram("triangle", "integral"))
    print("'apple' & 'pale':", is_anagram("apple", "pale"))
