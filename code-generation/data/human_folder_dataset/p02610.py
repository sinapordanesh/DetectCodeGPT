import heapq
from collections import defaultdict


def solve(N, klrs):
    # ベースの嬉しさは sum_i min(Li, Ri)
    # (1) Li > Ri なるラクダ
    #   なるべく先頭側に寄せることで追加の嬉しさを獲得できる
    # (2) Li < Ri なるラクダ
    #   なるべく末尾側に寄せることで追加の嬉しさを獲得できる
    # => (1), (2) それぞれで追加できる嬉しさの最大値を求めてベースに足す
    left_camels, right_camels = defaultdict(list), defaultdict(list)
    for i, (k, l, r) in enumerate(klrs):
        if l > r:
            left_camels[k].append(i)
        elif l < r:
            right_camels[k + 1].append(i)
    # (1)
    que = []
    for k in range(N):
        for i in left_camels[k]:
            _, l, r = klrs[i]
            heapq.heappush(que, l - r)
        while len(que) > k + 1:
            heapq.heappop(que)
    p_1 = 0
    while len(que) > 0:
        p_1 += heapq.heappop(que)    
    # (2)
    que = []
    for k in range(N - 1, -1, -1):
        for i in right_camels[k]:
            _, l, r = klrs[i]
            heapq.heappush(que, r - l)
        while len(que) > N - k:
            heapq.heappop(que)
    p_2 = 0
    while len(que) > 0:
        p_2 += heapq.heappop(que)
    return p_1 + p_2 + sum(min(l, r) for _, l, r in klrs)


def main():
    T = int(input())
    ans = [0] * T
    for t in range(T):
        N = int(input())
        klrs = list()
        for _ in range(N):
            k, l, r = map(int, input().split())
            klrs.append([k - 1, l, r])
        ans[t] = solve(N, klrs)
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()