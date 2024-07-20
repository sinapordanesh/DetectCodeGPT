def smallest_sequence(K, A):
    ans = []
    for i in range(K):
        ans.extend([i+1]*A[i])
    for i in range(K):
        sub = ans[i:i+K]
        if len(set(sub)) != K:
            return -1
    return ' '.join(map(str, ans))