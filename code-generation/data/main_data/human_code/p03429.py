import sys
input = sys.stdin.readline

import numpy as np

N,M,A,B = map(int,input().split())

def solve(N,M,A,B):
    grid = np.full((N,M),'.',dtype='U1')
    put_row = np.full((N,M-1),10**9,dtype=np.int32)
    if N%2 == 0:
        for n in range(0,M//2):
            put_row[:,n+n] = np.arange(N*n,N*(n+1))
    elif M%2 == 0:
        # N-1行目を埋めたあと、2個ずつ
        put_row[-1,::2] = np.arange(M//2)
        x = M//2
        for n in range(M//2):
            put_row[:-1,n+n] = np.arange(x,x+N-1)
            x += N-1
    else:
        # N-1行目を右優先で埋めたあと、左上から
        put_row[-1,1::2] = np.arange(M//2)
        x = M//2
        for n in range(M//2):
            put_row[0,n+n] = x
            put_row[1:-1,n+n+1] = np.arange(x+1,x+N-1)[::-1]
            x += N-1
    # 置くべき優先度を定義し終わった
    x,y = np.where(put_row < A)
    if len(x) != A:
        print('NO')
        return
    grid[x,y] = '<'
    grid[x,y+1] = '>'
    # 空きます
    put_col = (grid == '.')
    # 下も空いている（上側としておける）
    put_col[:-1] &= put_col[1:]
    put_col[-1] = 0
    for n in range(1,N):
        # ひとつ上から置けるならやめる
        put_col[n] &= ~put_col[n-1]
    x,y = np.where(put_col)
    x = x[:B]; y = y[:B]
    if len(x) != B:
        print('NO')
        return
    grid[x,y] = '^'
    grid[x+1,y] = 'v'
    print('YES')
    print('\n'.join(''.join(row) for row in grid))
    return

solve(N,M,A,B)