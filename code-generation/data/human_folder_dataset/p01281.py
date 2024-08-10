def solve():
    H, W = map(int, input().split())
    if H == 0:
        return False
    if H*W % 2 == 1:
        print(0)
        return True
    state = [[-1]*W for i in range(H)]
    def dfs(k):
        if k == H*W:
            return 1
        i, j = divmod(k, W)
        if state[i][j] != -1:
            return dfs(k+1)
        if i > 0 and j > 0 and state[i-1][j-1] != state[i-1][j] != state[i][j-1] != state[i-1][j-1]:
            return 0
        r = 0
        state[i][j] = k
        if i+1 < H:
            state[i+1][j] = k
            r += dfs(k+1)
            state[i+1][j] = -1
        if j+1 < W and state[i][j+1] == -1:
            state[i][j+1] = k
            r += dfs(k+1)
            state[i][j+1] = -1
        state[i][j] = -1
        return r
    print(dfs(0))
    return True
while solve():
    ...
