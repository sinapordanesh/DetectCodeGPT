def solve():
    from itertools import combinations
    from sys import stdin
    f_i = stdin
    
    def dfs(base, stones):
        key = tuple(stones)
        if key in rec:
            return set((base + l, base + r) for l, r in rec[key])
        
        edges = set()
        positions = set()
        for i in range(1, len(stones)):
            for tpl in combinations(stones, i):
                s1 = list(tpl)
                s2 = stones[:]
                for s in s1:
                    s2.remove(s)
                
                w1 = sum(s1)
                w2 = sum(s2)
                w = w1 + w2
                
                b1 = base - w2 / w
                b2 = base + w1 / w
                
                left_tree_ends = dfs(b1, s1)
                right_tree_ends = dfs(b2, s2)
                
                for ll, lr in left_tree_ends:
                    for rl, rr in right_tree_ends:
                        if ll < rl:
                            l = ll
                        else:
                            l = rl
                        if lr < rr:
                            r = rr
                        else:
                            r = lr
                        edges.add((l - base, r - base))
                        positions.add((l, r))
        
        rec[key] = edges
        return positions
    
    num = int(f_i.readline())
    
    rec = dict()
    for i in range(num):
        r = float(f_i.readline())
        s = int(f_i.readline())
        
        stones = sorted(int(f_i.readline()) for i in range(s))
        
        for stone in stones:
            rec[(stone,)] = {(0, 0)}
        
        edge_set = dfs(0, stones)
        try:
            ans = max(b - a for a, b in edge_set if b - a < r)
            print(ans)
        except ValueError:
            print(-1)

solve()
