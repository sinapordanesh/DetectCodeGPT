from itertools import accumulate

def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    
    nonzeros = [1]
    for a in As:
        ndp = nonzeros[-1]
        if a <= K:
            ndp |= (nonzeros[-1] % (1 << (K-a))) << a
        nonzeros.append(ndp)
    dp = [0] * (K+1)
    dp[0] = 1
    acc = list(accumulate(dp)) + [0]
    ans = 0
    for i in range(N, 0, -1):
        a = As[i-1]
        ndp = []
        for j in range(K+1):
            t = dp[j] if j < a else dp[j] + dp[j-a]
            ndp.append(0 if t == 0 else 1)
        dp = ndp
        if a < K:
            nonzero = nonzeros[i-1]
            for y in range(K+1):
                if nonzero & 1:
                    t = K-y-a-1
                    if acc[K-y-1] > acc[t if t >= 0 else -1]:
                        break
                nonzero >>= 1
            else:
                ans += 1
        acc = list(accumulate(dp)) + [0]
    
    print(ans)

main()
