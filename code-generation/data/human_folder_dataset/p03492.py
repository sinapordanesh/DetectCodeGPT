from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    def k_fix_way(com_n, com_r):
        if (com_n, com_r) in kmemo:
            return kmemo[(com_n, com_r)]
        res = kmemo[(com_n, com_r)] = fac[com_n] * inv[com_n - com_r] * fac[com_n] * inv[com_r] * inv[
            com_n - com_r] % md
        return res

    kmemo = {}

    def centroid(u=0, pu=-1):
        res = []
        is_centroid = True
        u_nodes = 1
        for cu in to[u]:
            if cu == pu: continue
            res += centroid(cu, u)
            cu_nodes = n_nodes[cu]
            if cu_nodes > n / 2: is_centroid = False
            u_nodes += cu_nodes
        n_nodes[u] = u_nodes
        if n - u_nodes > n / 2: is_centroid = False
        if is_centroid: res.append(u)
        return res

    md = 10 ** 9 + 7
    to = defaultdict(list)
    n = int(input())
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        to[u].append(v)
        to[v].append(u)
    # 部分木の頂点数を記録しながら重心を求める
    n_nodes = [0] * n
    cc = centroid()
    # print(cc)
    # 階乗の準備
    n_max = n
    fac = [1]
    inv = [1] * (n_max + 1)
    k_fac_inv = 1
    for i in range(1, n_max + 1):
        k_fac_inv = k_fac_inv * i % md
        fac.append(k_fac_inv)
    k_fac_inv = pow(k_fac_inv, md - 2, md)
    for i in range(n_max, 1, -1):
        inv[i] = k_fac_inv
        k_fac_inv = k_fac_inv * i % md
    # 重心が2つの（グラフを二等分できる）場合
    if len(cc) == 2:
        print(pow(fac[n // 2], 2, md))
        exit()
    # 重心が1つの場合
    # サブツリーの頂点数のリストsubtree_node_n作成
    subtree_node_n = []
    c = cc[0]
    for u in to[c]:
        u_nodes = n_nodes[u]
        if u_nodes > n / 2: continue
        subtree_node_n.append(u_nodes)
    if c != 0: subtree_node_n.append(n - n_nodes[c])
    # print(subtree_node_n)

    # dp[i][j]をi番目のサブツリーまでみて、j個の頂点を固定したときの決め方として求める
    dp = [0] * n
    dp[0] = 1
    for i, node_n in enumerate(subtree_node_n):
        for j in range(n - 1, -1, -1):
            pre = dp[j]
            if pre == 0: continue
            for k in range(node_n, 0, -1):
                dp[j + k] = (dp[j + k] + pre * k_fix_way(node_n, k)) % md
    # print(dp)
    # 包除原理
    ans = 0
    coff = 1
    for j in range(n):
        ans = (ans + coff * dp[j] * fac[n - j]) % md
        coff *= -1
    print(ans)

main()
