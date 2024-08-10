def min_operations(S, K):
    if len(S) == 1:
        return K // 2
    elif S[0] == S[-1]:
        return ((K - 1) * sum(a == b for a, b in zip(S, S[1:])) + 1) // 2
    else:
        return (sum(a == b for a, b in zip(S, S[1:])) * K) // 2

S, K = input().split()
S = str(S)
K = int(K)
print(min_operations(S, K))