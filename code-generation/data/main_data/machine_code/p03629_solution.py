def shortest_non_subsequence(A):
    for i in range(26):
        c = chr(ord('a') + i)
        if c not in A:
            return c
        
A = input()
print(shortest_non_subsequence(A))