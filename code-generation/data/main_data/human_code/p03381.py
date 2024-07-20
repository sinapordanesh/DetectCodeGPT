def main():
    N = int(input())
    B = [(b, i) for i, b in enumerate(map(int,input().split()))]
    B.sort()
    m2 = B[N//2][0]
    m1 = B[N//2-1][0]
    if m1 == m2:
        for i in range(N):
            print(m1)
        return

    ans = [0] * N
    for b, i in B:
        if b <= m1:
            ans[i] = m2
        else:
            ans[i] = m1
    print('\n'.join(map(str,ans)))
    # print(B)
# 1 2 2 2 
# 1 1 1 1 
main()