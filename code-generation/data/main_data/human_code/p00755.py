import copy
import itertools
import sys

if sys.version[0] == '2':
    range, input = xrange, raw_input

drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
C_NUM = 6

def dfs(r, c, now_c, next_c):
    tmp_board[r][c] = next_c
    for dr, dc in drc:
        nr, nc = r + dr, c + dc
        if 0 <= nr < H and 0 <= nc < W and tmp_board[nr][nc] == now_c:
            dfs(nr, nc, now_c, next_c)


while True:
    H, W, C = map(int, input().split())
    if not (H | W | C):
        break
    board = [[int(x) - 1 for x in input().split()] for _ in range(H)]
    ans = 0
    for ope in itertools.product(range(C_NUM), repeat=5):
        # print(ope)
        if ope[0] == board[0][0] or ope[-1] != C - 1 or any(ope[i] == ope[i + 1] for i in range(4)):
            continue
        tmp_board = copy.deepcopy(board)
        for color in ope:
            dfs(0, 0, tmp_board[0][0], color)
        dfs(0, 0, tmp_board[0][0], -1)
        cand = sum(row.count(-1) for row in tmp_board)
        if cand > ans:
            ans = cand
    print(ans)