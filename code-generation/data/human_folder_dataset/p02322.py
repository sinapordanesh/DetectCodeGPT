def main():
    from collections import deque
    from functools import cmp_to_key
    
    N, W, *A = map(int, open(0).read().split())
    A = [list(a) for a in zip(*[iter(A)]*3)]

    Vmax = max(v for v, w, m in A)
    Vsum = 0
    B = []
    for i, (v, w, m) in enumerate(A):
        m_upper = min(m, Vmax-1)
        m_rest = m - m_upper
        A[i][2] = m_upper
        if m_rest:
            B.append((v, w, m_rest))
        Vsum += v*m_upper

    INF = 1<<60
    dp = [INF]*(Vsum+1)
    dp[0] = 0

    for v, w, m in A:
        for ofs in range(v):
            q = deque()
            for j in range(Vsum+1):
                vj = ofs + j*v
                if vj > Vsum:
                    break
                src = dp[vj] - j*w
                while q and q[-1][1] >= src:
                    q.pop()
                q.append((j, src))

                if q:
                    ni, nw = q[0]
                    dp[vj] = nw + j*w
                    if ni == j - m:
                        q.popleft()
    
    B.sort(key=cmp_to_key(lambda a, b: -1 if a[0]*b[1] > a[1]*b[0] else 1))

    ans = 0
    for V, d in enumerate(dp):
        if d > W:
            continue
        W_rest = W - d
        for v, w, m in B:
            n_item = min(m, W_rest//w)
            if n_item:
                V += n_item * v
                W_rest -= n_item * w
        if ans < V:
            ans = V

    print(ans)

if __name__ == '__main__':
    main()
