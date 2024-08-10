def max_targets_destroyed():
    H, W, M = map(int, input().split())
    targets = set()
    rows = [0] * H
    cols = [0] * W
    
    for _ in range(M):
        h, w = map(int, input().split())
        h -= 1
        w -= 1
        targets.add((h, w))
        rows[h] += 1
        cols[w] += 1
    
    max_rows = max(rows)
    max_cols = max(cols)
    
    ans = max_rows + max_cols
    
    for h in range(H):
        for w in range(W):
            if (h, w) in targets:
                continue
            if rows[h] + cols[w] > ans:
                ans = rows[h] + cols[w]
    
    print(ans)

max_targets_destroyed()