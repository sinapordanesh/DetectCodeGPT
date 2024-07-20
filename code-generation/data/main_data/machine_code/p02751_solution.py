def maximize_oddness(N, M):
    grid = [[1] * (2**M - 1) for _ in range(2**N - 1)]
    
    for row in grid:
        print(''.join(map(str, row)))

N, M = map(int, input().split())
maximize_oddness(N, M)