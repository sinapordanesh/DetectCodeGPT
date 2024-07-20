def naive_string_search(T, P):
    indices = []
    for i in range(len(T) - len(P) + 1):
        if T[i:i + len(P)] == P:
            indices.append(i)
    
    for index in indices:
        print(index)

# Sample Input 1
naive_string_search("aabaaa", "aa")

# Sample Input 2
naive_string_search("xyzz", "yz")

# Sample Input 3
naive_string_search("abc", "xyz")