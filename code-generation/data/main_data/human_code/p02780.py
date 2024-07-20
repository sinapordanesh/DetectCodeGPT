def calc_ex(P):
    sum = 0
    for p in range(1, P+1):
        sum += p
    return sum / P

def main():
    N, K = map(int,input().split())
    P = list(map(int,input().split()))
    accumP = [0] * (N + 1)
    for i in range(N):
        accumP[i+1] = accumP[i] + P[i]

    # 最大の区間を求める
    idx = 0
    sum = accumP[idx+K] - accumP[idx] 
    for i in range(0, N-K+1):
        if accumP[i+K] - accumP[i] > sum:
            idx = i
            sum = accumP[i+K] - accumP[i]
    
    
    ans = 0
    for i in range(idx, idx+K):
        ans += calc_ex(P[i])

    print(ans)

if __name__ == "__main__":
    main()