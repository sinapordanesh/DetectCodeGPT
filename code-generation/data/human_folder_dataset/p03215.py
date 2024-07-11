def dwacon5th_prelims_b():
    n, k = (int(x) for x in input().split())
    A = [int(x) for x in input().split()]
    B = []

    for i in range(n):
        cum = 0
        for a in A[i:]:
            cum += a
            B.append(cum)
    B.sort(reverse=True)

    bit = [0]*41
    cand = B.copy()
    for i in range(40, -1, -1):
        nx = []
        for b in cand:
            if (b >> i) & 1: nx.append(b)
        if len(nx) >= k:
            cand = nx.copy()
            bit[i] = 1

    ans = int(''.join([str(x) for x in reversed(bit)]), base=2)
    print(ans)

if __name__ == '__main__':
   dwacon5th_prelims_b()