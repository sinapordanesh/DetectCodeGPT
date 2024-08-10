drc = [(0, 1), (1, 0)]


def dfs(r, c):
    if (r, c) in memo:
        return memo[r, c]
    ret = ''
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if nr < H and nc < W and board[nr][nc].isdigit():
            cand = dfs(nr, nc)
            if len(cand) > len(ret) or (len(cand) == len(ret) and cand > ret):
                ret = cand
    memo[r, c] = board[r][c] + ''.join(ret)
    return board[r][c] + ret


while True:
    W, H = map(int, input().split())
    if not (W | H):
        break
    board = [input() for _ in range(H)]
    memo = dict()
    ans = ''
    for r in range(H):
        for c in range(W):
            if board[r][c].isdigit() and board[r][c] != '0':
                cand = dfs(r, c)
                if len(cand) > len(ans) or (len(cand) == len(ans) and cand > ans):
                    ans = cand
    print(ans)