def main():
    N, K = map(int, input().split())
    S = list(input())
    base = S[0]
    flag = False
    for i in range(0, N):
        if K == 0:
            break
        if S[i] != base and (not flag):
            flag = True
            S[i] = base
        elif S[i] != base and flag:
            S[i] = base
        elif S[i] == base and flag:
            flag = False
            K -= 1
        else:
            pass
    
    ans = 0
    for i in range(N-1):
        ans += S[i] == S[i+1]
    
    print(ans)
  
if __name__ == "__main__":
    main()
