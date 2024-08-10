from collections import deque
def main():
    I = {
        1: ((6, 0), (2, 1), (5, 2), (4, 3)),
        2: ((6, 3), (3, 1), (5, 3), (1, 3)),
        3: ((6, 2), (4, 1), (5, 0), (2, 3)),
        4: ((6, 1), (1, 1), (5, 1), (3, 3)),
        5: ((1, 0), (2, 0), (3, 0), (4, 0)),
        6: ((1, 2), (2, 2), (3, 2), (4, 2)),
    }
    J = [[6, 7, 8], [2, 5, 8], [0, 1, 2], [0, 3, 6]]
    D = [
        (1, 5, 2, 3, 0, 4), # 'U'
        (3, 1, 0, 5, 4, 2), # 'R'
        (4, 0, 2, 3, 5, 1), # 'D'
        (2, 1, 5, 0, 4, 3), # 'L'
    ]
    def rotate_dice(L, k):
        return tuple(L[e] for e in D[k])

    R = (5, 1, 2, 4, 3, 6)
    que = deque()
    dist = {R: 0}
    que.append(R)
    while que:
        s = que.popleft()
        d = dist[s]
        for i in range(4):
            t = rotate_dice(s, i)
            if t in dist:
                continue
            dist[t] = d+1
            que.append(t)

    C = [None]*6
    while 1:
        S = input()
        if S == '#':
            break
        C[0] = "".join([S, input(), input()])
        for i in range(5):
            C[i+1] = "".join([input() for i in range(3)])
        ans = 10
        for s, v in dist.items():
            a = s[0]; b = s[1]
            for k, (i, e) in enumerate(I[a]):
                if i == b:
                    j, f = I[a][k-2]
                    if any(C[i-1][k1] == '*' for k1 in J[e]) and any(C[j-1][k2] == '*' for k2 in J[f]):
                        ans = min(ans, v)
                    break
        print(ans)
        input()
main()
