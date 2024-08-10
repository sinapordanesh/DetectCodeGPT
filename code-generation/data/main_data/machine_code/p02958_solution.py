def can_sort_permutation(N, p):
    sorted_p = sorted(p)
    if p == sorted_p:
        return "YES"
    else:
        for i in range(N):
            for j in range(i+1, N):
                p_copy = p.copy()
                p_copy[i], p_copy[j] = p_copy[j], p_copy[i]
                if p_copy == sorted_p:
                    return "YES"
        return "NO"  

# Driver code
N = int(input())
p = list(map(int, input().split()))

print(can_sort_permutation(N, p))