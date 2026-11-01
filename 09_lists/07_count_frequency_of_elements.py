"""
Q7: Count frequency of each distinct element in a list without list.count() or collections.Counter.
"""

def count_frequencies(items):
    elements = []
    counts = []
    for x in items:
        found = False
        for i in range(len(elements)):
            if elements[i] == x:
                counts[i] += 1
                found = True
                break
        if not found:
            elements.append(x)
            counts.append(1)
    return list(zip(elements, counts))

if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print("Frequencies:", count_frequencies(arr))
