def solve(N, M, boxes):
    moves = 0
    for i in range(M):
        a, b, c = boxes[i]
        if a == b:
            moves += 0
        elif c >= 2:
            moves += 1
        else:
            moves += 2
    return moves if moves <= N else -1

# Input
N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(M)]

# Output
print(solve(N, M, boxes))