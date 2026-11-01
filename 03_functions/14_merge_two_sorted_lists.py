"""
Q14: Write a function to merge two sorted lists into one sorted list without sort().
"""

def merge_sorted_lists(list1, list2):
    merged = []
    
    n1 = 0
    for _ in list1:
        n1 += 1
    n2 = 0
    for _ in list2:
        n2 += 1
        
    i = 0
    j = 0
    while i < n1 and j < n2:
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
            
    while i < n1:
        merged.append(list1[i])
        i += 1
        
    while j < n2:
        merged.append(list2[j])
        j += 1
        
    return merged

if __name__ == "__main__":
    l1 = [1, 3, 5, 7]
    l2 = [2, 4, 6, 8, 10]
    print("Merged:", merge_sorted_lists(l1, l2))
