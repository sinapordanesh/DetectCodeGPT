def max_sum_picked_cards(N, H, W, cards):
    rows = [0] * (H+1)
    cols = [0] * (W+1)
    
    for r, c, a in cards:
        rows[r] = max(rows[r], a)
        cols[c] = max(cols[c], a)
    
    max_row = sum(sorted(rows, reverse=True)[:H])
    max_col = sum(sorted(cols, reverse=True)[:W])
    
    return max_row + max_col

# Input
N, H, W = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

# Output
print(max_sum_picked_cards(N, H, W, cards))