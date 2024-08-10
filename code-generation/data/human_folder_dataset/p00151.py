# Aizu Problem 00151: Grid
#
import sys, math, os, bisect

# read input:
PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")


def grid_length(n, grid):
    L = 0
    for row in grid:
        L = max(L, max([len(_) for _ in row.split('0')]))
    for c in range(n):
        col = ''.join([grid[r][c] for r in range(n)])
        L = max(L, max([len(_) for _ in col.split('0')]))
    for row in range(-n, 2 * n):
        diag = ''.join([grid[row+c][c] for c in range(n) if 0 <= row + c < n])
        L = max(L, max([len(_) for _ in diag.split('0')]))
        diag = ''.join([grid[row-c][c] for c in range(n) if 0 <= row - c < n])
        L = max(L, max([len(_) for _ in diag.split('0')]))
    return L

while True:
    n = int(input())
    if n == 0:
        break
    grid = [input().strip() for _ in range(n)]
    print(grid_length(n, grid))