n = int(input())
heights = list(map(int, input().split()))

def solve(heights, beg, end) -> int:
    if beg >= end: return 0
    try:
        idx = beg + heights[beg:end].index(0)
        return  solve(heights, beg, idx) + solve(heights, idx+1, end)
    except ValueError:
        pass
    
    minh = min(heights[beg:end])
    for i in range(beg, end):
        heights[i] -= minh
    return minh + solve(heights, beg, end)

cnt = solve(heights, 0, len(heights))
print(cnt)