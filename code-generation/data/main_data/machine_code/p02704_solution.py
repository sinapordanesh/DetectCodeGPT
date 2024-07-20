def find_matrix(N, S, T, U, V):
    for i in range(2**N):
        a = [[0]*N for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if S[j] == 0:
                    a[j][k] = a[j][k] & i
                else:
                    a[j][k] = a[j][k] | i
        for j in range(N):
            col_value = 0
            for k in range(N):
                if T[k] == 0:
                    col_value = col_value & a[k][j]
                else:
                    col_value = col_value | a[k][j]
            if col_value != V[j]:
                break
        else:
            return a
    return -1