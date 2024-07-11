def main():
    n = int(input())
    a = [int(input()) for _ in [0]*n]
    xor = 0
    for i in a:
        xor ^= i
    i = 1
    cnt = 0
    while True:
        if xor >= i:
            i *= 2
            cnt += 1
        else:
            break
    ans = 0
    for i in range(cnt-1, -1, -1):
        j = (xor & 2**i) // (2**i)
        if j == 1:
            for k in a:
                if (k & 2**i) // (2**i) == 1 and k % (2**i) == 0:
                    xor ^= k
                    xor ^= k-1
                    ans += 1
                    a.remove(k)
                    break
            else:
                print(-1)
                return 0
    print(ans)


main()