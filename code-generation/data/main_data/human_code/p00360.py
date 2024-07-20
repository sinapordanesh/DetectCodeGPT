import sys

def main():
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    s = SI()
    n = len(s)
    k = NI()

    def conv(x):
        return ord(x) - ord('a')

    bit = [0] * (n+1)

    def bit_add(i):
        while i <= n:
            bit[i] += 1
            i += i & (-i)

    def bit_sum(i):
        ret = 0
        while i > 0:
            ret += bit[i]
            i -= i & (-i)
        return ret

    z = [0] * n
    top = [-1] * 26
    nxt = [-1] * n
    bef = [-1] * 26
    for i in range(n):
        cv = conv(s[i])
        if bef[cv] >= 0:
            nxt[bef[cv]] = i
        bef[cv] = i
        if top[cv] < 0:
            top[cv] = i

    ans = []
    while k > 0:
        for i in range(26):
            if top[i] < 0: continue
            p = top[i]
            cost = p - bit_sum(p+1)
            if cost <= k:
                ans.append(chr(ord('a')+i))
                z[top[i]] = 1
                k -= cost
                top[i] = nxt[top[i]]
                bit_add(p+1)
                break
        else:
            break


    for i in range(n):
        if z[i] == 0: ans.append(s[i])
    print(*ans,sep='')


if __name__ == '__main__':
    main()
