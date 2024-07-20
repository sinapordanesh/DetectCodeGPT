def smallest_permutation(N, K, P):
    P = [int(x) for x in P.split()]
    for i in range(N - 1):
        for j in range(i + K, min(i + K + 1, N)):
            if abs(P[i] - P[j]) == 1:
                P[i], P[j] = P[j], P[i]
    
    return P

N, K = map(int, input().split())
P = input()
result = smallest_permutation(N, K, P)
for num in result:
    print(num)