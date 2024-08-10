def A():
    n, x, t = map(int, input().split())
    print(t * ((n+x-1)//x))

def B():
    n = list(input())
    s = 0
    for e in n:
        s += int(e)
    print("Yes" if s % 9 == 0 else "No")

def C():
    int(input())
    a = list(map(int, input().split()))
    l = 0
    ans = 0
    for e in a:
        if e < l: ans += l - e
        l = max(l, e)
    print(ans)

def E():
    h, w, m = map(int, input().split())
    row = [0] * h
    col = [0] * w
    exist = set([])
    th = 1000000000
    for i in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        row[x] += 1
        col[y] += 1
        exist.add(x*th + y)

    max_row = max(row)
    max_col = max(col)
    candi_row = []
    candi_col = []
    for i in range(h):
        if row[i] == max_row: candi_row.append(i)
    for i in range(w):
        if col[i] == max_col: candi_col.append(i)

    ans = max_row + max_col
    for x in candi_row:
        for y in candi_col:
            if x*th + y in exist: continue
            print(ans)
            return
    print(ans - 1)

E()
