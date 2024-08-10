def main():
    S = list(input())
    K = int(input())
    cnt = 0
    if K == 1:
        T = S
        for i in range(len(T)-1):
            if T[i] == T[i+1]:
                T[i+1] = '.'
        ans = T.count('.')
        print(ans)
        return

    if len(S) == 1:
        ans = max(0, (K - (K%2==1))//2)
        print(ans)
        return

    if len(set(S)) == 1:
        tmp = len(S)*K
        tmp = tmp - (tmp%2 == 1)
        ans = tmp//2
        print(ans)
        return

    T3 = S + S + S
    for i in range(len(T3)-1):
        if T3[i] == T3[i+1]:
            T3[i+1] = '.'
    
    T2aster = T3[len(S):(2*len(S))].count('.')
    T3aster = T3.count('.')
    ans = T3aster + T2aster * (K-3)
    print(ans)

if __name__ == "__main__":
    main()
