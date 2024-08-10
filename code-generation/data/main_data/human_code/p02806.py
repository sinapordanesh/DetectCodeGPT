def main():
    N = int(input())
    st = [list(input().split()) for i in range(N)]
    X = input()
    ans = 0
    for i in range(N):
        if st[i][0] == X:
            i += 1
            break

    for j in range(i,N,1):
        ans += int(st[j][1])

    return ans

print(main())
