# 【条件1】各ノードに記載する数字が全部正の整数
# start: v (> 0) として
# 1: s1 - v > 0            =>  s1 > v
# 2: s2 - s1 + v > 0       =>  v > s1 - s2
# 3: s3 - s2 + s1 - v > 0  =>  s1 - s2 + s3 > v
# 4: ...
# -> max{0, s1 - s2, s1 - s2 + s3 - s4, ...} < v < min{s1, s1 - s2 + s3, ...}
#    なので、max{0, 右辺 - 左辺 - 1} が答え。
# 【条件2】 loopがあったらそのloop上で s1 - s2 + s3 - s4 + ... = 0 じゃないとダメ
# あるノードまで複数の行き方で行けた場合、
# 偶奇が同じケースなら
#   s1 - s2 + s3 - ... = s'1 - s'2 + s'3 - ...
# が成り立っていれば整合性は保たれる。
# 偶奇が異なるケースなら、
# v = (奇のs + 遇のs) / 2
# の時のみ整合性が保たれる。
from collections import defaultdict, deque


def main():
    INF = 10 ** 15
    N, M = map(int, input().split())
    S = defaultdict(int)
    adj = defaultdict(list)
    for _ in range(M):
        u, v, s = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        S[(u, v)], S[(v, u)] = s, s
    even_sum_s, odd_sum_s = [- INF] * N, [INF] * N
    start = 0
    even_sum_s[start] = 0
    que = deque([(start, -1, 0, 0)])  # (node, parent, dist from start, sum of signed `s`)
    unique_n = -1
    # DFS
    while len(que) > 0:
        node, parent_node, dist, sum_s = que.pop()
        for next_node in adj[node]:
            if parent_node == next_node:
                continue
            next_dist = dist + 1
            if next_dist % 2 == 1:
                next_sum_s = sum_s + S[(node, next_node)]
                if even_sum_s[next_node] != - INF:
                    s = next_sum_s + even_sum_s[next_node]
                    if s < 2 or s % 2 != 0 or (unique_n > 0 and unique_n != s // 2):
                        print(0)
                        return
                    unique_n = s // 2
                if odd_sum_s[next_node] == INF:
                    odd_sum_s[next_node] = next_sum_s
                    que.append((next_node, node, next_dist, next_sum_s))
                else:
                    if odd_sum_s[next_node] != next_sum_s:
                        print(0)
                        return
            else:
                next_sum_s = sum_s - S[(node, next_node)]
                if odd_sum_s[next_node] != INF:
                    s = odd_sum_s[next_node] + next_sum_s
                    if s < 2 or s % 2 != 0 or (unique_n > 0 and unique_n != s // 2):
                        print(0)
                        return
                    unique_n = s // 2
                if even_sum_s[next_node] == - INF:
                    even_sum_s[next_node] = next_sum_s
                    que.append((next_node, node, next_dist, next_sum_s))
                else:
                    if even_sum_s[next_node] != next_sum_s:
                        print(0)
                        return
    lower, upper = max(even_sum_s), min(odd_sum_s)
    if unique_n > 0:
        if lower < unique_n < upper:
            print(1)
        else:
            print(0)
    else:
        print(max(0, upper - lower - 1))


if __name__ == '__main__':
    main()