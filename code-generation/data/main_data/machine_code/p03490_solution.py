def robot(s, x, y):
    from collections import deque
    s = deque(s)
    n = len(s)
    s.appendleft('F')
    
    xt, yt = [], []
    xflag = yflag = False
    cnt = 0
    for i in range(n+1):
        if s[i] == 'F':
            cnt += 1
        else:
            if cnt:
                if not xflag:
                    xt.append(cnt)
                    xflag = True
                else:
                    yt.append(cnt)
                    yflag = True
                cnt = 0
    
    qx, qy = [0], [0]
    for i in range(len(xt)):
        nx, ny = [], []
        for j in range(-2500, 2501):
            if 0 <= j + xt[i] <= 5000 and qx[-1] + j <= 5000:
                nx.append(j + xt[i])
            if 0 <= j + yt[i] <= 5000 and qy[-1] + j <= 5000:
                ny.append(j + yt[i])
        qx, qy = list(set(nx)), list(set(ny))
    
    return "Yes" if x in qx and y in qy else "No"

s, x, y = input().split()
print(robot(s, int(x), int(y)) )