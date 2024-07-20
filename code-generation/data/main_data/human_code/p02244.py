N = 8
FREE = 1
NOT_FREE = -1

def initialize():
    row = [FREE] * N
    col = [FREE] * N
    dpos = [FREE] * (2 * N - 1)
    dneg = [FREE] * (2 * N - 1)
    return row, col, dpos, dneg


def printBoard(x, row):
    for i in range(N):
        for j in range(N):
            if x[i][j]:
                if row[i] != j:
                    return
    for i in range(N):
        line = ''
        for j in range(N):
            if row[i] == j:
                line += 'Q'
            else:
                line += '.'
        print(line)


def recursive(i, x, row, col, dpos, dneg):
    if i == N:
        printBoard(x, row)
        return

    for j in range(N):
        if (NOT_FREE == col[j] or
            NOT_FREE == dpos[i + j] or
            NOT_FREE == dneg[i - j + N - 1]):
            continue
        row[i] = j
        col[j] = NOT_FREE
        dpos[i + j] = NOT_FREE
        dneg[i - j + N - 1] = NOT_FREE
        recursive(i+1, x, row, col, dpos, dneg)
        row[i] = FREE
        col[j] = FREE
        dpos[i + j] = FREE
        dneg[i - j + N - 1] = FREE


if __name__ == '__main__':
    row, col, dpos, dneg = initialize()
    x = [[False] * N for i in range(N)]
    k = int(input())
    for i in range(k):
        r, c = [int(v) for v in input().split()]
        x[r][c] = True

    recursive(0, x, row, col, dpos, dneg)
