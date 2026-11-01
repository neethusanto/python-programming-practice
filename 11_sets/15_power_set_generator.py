"""
Q15: Generate the power set (all subsets) of a set without itertools.combinations.
"""

def generate_power_set(s):
    elements = []
    for x in s:
        elements.append(x)
        
    power_set = [set()]
    for elem in elements:
        new_subsets = []
        for subset in power_set:
            new_sub = set(subset)
            new_sub.add(elem)
            new_subsets.append(new_sub)
        power_set = power_set + new_subsets
    return power_set

if __name__ == "__main__":
    sample = {1, 2, 3}
    p_set = generate_power_set(sample)
    print(f"Power set of {sample} ({len(p_set)} subsets):")
    for sub in p_set:
        print(" ", sub)
