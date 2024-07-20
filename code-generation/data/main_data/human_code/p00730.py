ans_list = []
def make_pieces(w, d, s):
    if w == 0 and d == 0:
        print(w, d, s)
    s %= (2 * w + 2 * d)
    while True:
        if w > s:
            return [s, d], [w - s, d]
        s -= w
        if d > s:
            return [w, s], [w, d - s]
        s -= d
        if w > s:
            return [w - s, d], [s, d]
        s -= w
        if d > s:
            return [w, s], [w, d - s]
        s -= d


while True:
    n, w, d = map(int, input().split())
    P = [[w, d]]
    if n == 0 and w == 0 and d == 0:
        break
    for i in range(n):
        p, s = map(int, input().split())
        new_pieces = make_pieces(P[p - 1][0], P[p - 1][1], s)
        #print(new_pieces)
        if new_pieces[0][0] * new_pieces[0][1] < new_pieces[1][0] * new_pieces[1][1]:
            P = P[:p - 1] + P[p:] + [new_pieces[0]] + [new_pieces[1]]
        else:
            P = P[:p - 1] + P[p:] + [new_pieces[1]] + [new_pieces[0]]
        #print(P)

    S_list = []
    for i in P:
        S_list.append(i[0] * i[1])

    S_list.sort()
    ans_list.append(S_list)

for i in range(len(ans_list)):
    I = ans_list[i]
    for j in range(len(I)):
        J = I[j]
        if j == len(I) - 1:
            print(J, end = "")
        else:
            print(J, end=" ")
    print()
