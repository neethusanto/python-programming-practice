"""
Q14: Filter all palindrome words from a list of words using lambda and filter().
"""

def filter_palindromes(words):
    check_pal = lambda w: w == "".join([w[len(w) - 1 - i] for i in range(len(w))])
    return list(filter(check_pal, words))

if __name__ == "__main__":
    word_list = ["racecar", "hello", "madam", "world", "noon", "python"]
    print("Palindromes:", filter_palindromes(word_list))
