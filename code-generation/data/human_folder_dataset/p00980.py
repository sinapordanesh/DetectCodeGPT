def isValid(row, col, ROWS, COLS):
    return row >= 0 and row < ROWS and col >= 0 and col < COLS

def isSteep(board, row, col, ROWS, COLS):
    global adjR, adjC

    h = board[row][col]
    for i in range(4):
        rr = row + adjR[i]
        cc = col + adjC[i]
        if isValid(rr, cc, ROWS, COLS):
            diff = abs(h - board[rr][cc])
            if diff > 1:
                return True
    return False

def update(board, row, col, ROWS, COLS):
    global adjR, adjC, given
    arr = []

    h = board[row][col]
    for i in range(4):
        rr = row + adjR[i]
        cc = col + adjC[i]
        if (rr, cc) in given:
            continue
        if isValid(rr, cc, ROWS, COLS):
            if board[rr][cc] == None or board[rr][cc] < h - 1:
                board[rr][cc] = h - 1
                arr.append((rr, cc))
    return arr

if __name__ == '__main__':
    COLS, ROWS, N = list(map(int, input().split()))

    board = [ [ None for _ in range(COLS) ] for _ in range(ROWS) ]
    plist = []

    adjR = [-1, 0, 0, 1]
    adjC = [0, -1, 1, 0]

    given = set()

    for _ in range(N):
        c, r, h = list(map(int, input().strip().split()))
        board[r - 1][c - 1] = h
        plist.append((r-1, c-1))
        given.add((r-1, c-1))

    while len(plist) > 0:
        row, col = plist.pop(0)
        updated = update(board, row, col, ROWS, COLS)
        plist.extend(updated)

    isPossible = True
    total = 0
    for r in range(ROWS):
        for c in range(COLS):
            isPossible = isPossible and not isSteep(board, r, c, ROWS, COLS)
            if not isPossible:
                break
            total += board[r][c]
        if not isPossible:
            break

    print(total if isPossible else "No")
