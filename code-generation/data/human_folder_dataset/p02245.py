from collections import deque

N = 3
N2 = 9

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dirc = ['u', 'l', 'd', 'r']

class Puzzle:
    def __init__(self, f=None, space=None, path=None):
        if f is None:
            self.f = []
        else:
            self.f = f
        self.space = space
        self.path = path

    def __lt__(self, p):
        for i in range(N2):
            if self.f[i] == p.f[i]:
                continue
            return self.f[i] > p.f[i]
        return False


def isTarget(p):
    for i in range(N2):
        if p.f[i] != (i + 1):
            return False
    return True


def bfs(s):
    q = deque()
    dic = {}
    s.path = ''
    q.append(s)
    dic[tuple(s.f)] = True

    while len(q) != 0:
        u = q.popleft()
        if isTarget(u):
            return u.path
        sx = u.space // N
        sy = u.space % N
        for r in range(4):
            tx = sx + dx[r]
            ty = sy + dy[r]
            if tx < 0 or ty < 0 or tx >= N or ty >= N:
                continue
            v = Puzzle(u.f[:], u.space, u.path)
            v.f[u.space], v.f[tx * N + ty] = v.f[tx * N + ty], v.f[u.space]
            v.space = tx * N + ty
            key = tuple(v.f)
            if key not in dic:
                dic[key] = True
                v.path += dirc[r]
                q.append(v)

    return 'unsolvable'


if __name__ == '__main__':
    p = Puzzle()
    for i in range(N):
        line = [int(v) for v in input().split()]
        for j in range(N):
            if line[j] == 0:
                line[j] = N2
                p.space = i * N + j
        p.f.extend(line)

    ans = bfs(p)
    print(len(ans))
