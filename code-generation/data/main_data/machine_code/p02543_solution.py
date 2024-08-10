def solve(N, K, X, Q, queries):
    ans = []
    for i in range(Q):
        L, R = queries[i]
        cnt = 1
        for j in range(L, R):
            if X[j+1] - X[j] >= K:
                cnt += 1
        ans.append(cnt)
    return ans

N, K = map(int, input().split())
X = list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

result = solve(N, K, X, Q, queries)
for res in result:
    print(res)