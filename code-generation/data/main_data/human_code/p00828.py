dirs = [
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(1,-1,0),
    (0,1,1),(0,1,-1),
    (1,0,1),(-1,0,1),
    (1,1,1),(1,1,-1),
    (1,-1,1),(1,-1,-1)
]
def judge(x,y,z):
    c = pegs[x][y][z]
    for dx,dy,dz in dirs:
        sq = 1
        for _m in (1,-1):
            m = _m
            while True:
                mx,my,mz = x + m*dx, y + m*dy, z + m*dz
                if any(map(lambda l:not(0<=l<N), (mx,my,mz))): break
                if pegs[mx][my][mz] == c:
                    sq += 1
                    if sq >= M:
                        return c
                else:
                    break
                m += _m
    return 0

while True:
    N,M,P = map(int,input().split())
    if N == 0: break
    moves = [tuple(map(lambda x:int(x)-1, input().split())) for i in range(P)]
    pegs = [[[0 for z in range(N)] for y in range(N)] for x in range(N)]
    turn = 1
    for i,(x,y) in enumerate(moves):
        z = pegs[x][y].index(0)
        pegs[x][y][z] = turn
        turn *= -1
        c = judge(x,y,z)
        if c != 0:
            winner = 'Black' if c > 0 else 'White'
            print(winner + ' ' + str(i+1))
            break
    else:
        print('Draw')