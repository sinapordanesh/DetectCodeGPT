import sys
from heapq import heappop, heappush, heapify

def main():
    input = sys.stdin.readline
    
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ls = [b-a for a, b in zip(A, B)]
    q_m = [-v for v in ls[1:-1] if v < 0]
    q_p = [v for v in ls[1:-1] if v >= 0]
    heapify(q_m)
    heapify(q_p)
    sum_A = sum(A)
    sum_q_p = sum(q_p)
    to_remove = set()
    odd = len(q_p) % 2
    Ans = []
    ans = sum_A + sum_q_p - (min(q_p[0], q_m[0]) if odd else 0)
    for _ in range(Q):
        p, x, y = map(int, input().split())
        p -= 1
        v = y-x
        sum_A += x - A[p]
        if p==0 or p==2*N-1:
            ans += x - A[p]
            Ans.append(ans)
            A[p] = x
            continue
        A[p] = x
        odd ^= (ls[p] >= 0) ^ (v >= 0)
        if v >= 0:
            sum_q_p += v
        if ls[p] >= 0:
            sum_q_p -= ls[p]
        to_remove.add(ls[p])
        ls[p] = v
        if v >= 0:
            heappush(q_p, v)
        else:
            heappush(q_m, -v)
        ans = sum_q_p + sum_A
        if odd:
            while q_p[0] in to_remove:
                to_remove.remove(heappop(q_p))
            while -q_m[0] in to_remove:
                to_remove.remove(-heappop(q_m))
            ans -= min(q_p[0], q_m[0])
        Ans.append(ans)
    print("\n".join(map(str, Ans)))

main()
