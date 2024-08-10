from math import sqrt

def getcircle(nee, R): #針にぶつかる範囲の円
    (x, y, h) = nee
    if R <= h:
        return (x, y, R)
    r = sqrt(R**2 - (R-h)**2)
    return (x, y, r)
    
def crosscircle(c1, c2): #円の交点
    (x1, y1, r1) = c1
    (x2, y2, r2) = c2
    if (x1-x2)**2 + (y1-y2)**2 > (r1+r2)**2:
        return ()
    elif x1 == x2 and y1 == y2:
        return ()
    elif (x1-x2)**2 + (y1-y2)**2 == (r1+r2)**2:
        x = (x1*r2+x2*r1)/(r1+r2)
        y = (y1*r2+y2*r1)/(r1+r2)
        return ((x, y),)
    elif y1 == y2:
        x = (r1**2-r2**2-x1**2+x2**2)/(2*(x2-x1))
        if y1**2-(y1**2-r1**2+(x-x1)**2) >= 0:
            yans1 = y1+sqrt(y1**2-(y1**2-r1**2+(x-x1)**2))
            yans2 = y1-sqrt(y1**2-(y1**2-r1**2+(x-x1)**2))
            return ((x, yans1), (x, yans2))
        else:
            return ()
    elif x1 == x2:
        y = (r1**2-r2**2-y1**2+y2**2)/(2*(y2-y1))
        if x1**2-(x1**2-r1**2+(y-y1)**2) >= 0:
            xans1 = x1+sqrt(x1**2-(x1**2-r1**2+(y-y1)**2))
            xans2 = x1-sqrt(x1**2-(x1**2-r1**2+(y-y1)**2))
            return ((xans1, y), (xans2, y))
        else:
            return ()
    else:
        A = ((x1-x2)/(y1-y2))**2 + 1
        B = (x1-x2)*(r1**2-r2**2-x1**2+x2**2+(y1-y2)**2)/(y1-y2)**2 - 2*x1
        C = ((r1**2-r2**2-x1**2+x2**2+(y1-y2)**2)/(2*(y1-y2)))**2 + x1**2 - r1**2
        if B**2 - 4*A*C >= 0:
            xans1 = (-B+sqrt(B**2-4*A*C))/(2*A)
            xans2 = (-B-sqrt(B**2-4*A*C))/(2*A)
            yans1 = -((r1**2-r2**2-x1**2+x2**2-y1**2+y2**2))/(2*(y1-y2))-xans1*(x1-x2)/(y1-y2)
            yans2 = -((r1**2-r2**2-x1**2+x2**2-y1**2+y2**2))/(2*(y1-y2))-xans2*(x1-x2)/(y1-y2)
            return ((xans1, yans1), (xans2, yans2))  
        else:
            return ()
        

while True:
    n, w = map(int, input().split())
    if n == w == 0:
        break
    nees = [tuple(map(float, input().split())) for i in range(n)]
    eps = 0.000001
    U = 130
    L = 0
    while U - L > 0.0001:
        ok = False
        R = (U+L)/2
        cirs = []
        points = []
        if R > w:
            l = sqrt(R**2 - (R-w)**2) #球が壁にぶつからない範囲の正方形(l<=x<=100-l, l<=y<=100-l)
        else:
            l = R
        if l >= 100-l:
            U = R
            continue
        for nee in nees:
            c = getcircle(nee, R)
            cirs.append(c)
        for c in cirs: #正方形と円の交点をリストに入れる
            (x, y, r) = c
            if abs(l-x) <= r:
                if l <= y+sqrt(r**2-(x-l)**2) <= 100-l:
                    points.append((l,y+sqrt(r**2-(x-l)**2)))
                if l <= y-sqrt(r**2-(x-l)**2) <= 100-l:
                    points.append((l,y-sqrt(r**2-(x-l)**2)))
            if abs(l-y) <= r:
                if l <= x+sqrt(r**2-(y-l)**2) <= 100-l:
                    points.append((x+sqrt(r**2-(y-l)**2),y))
                if l <= x-sqrt(r**2-(y-l)**2) <= 100-l:
                    points.append((x-sqrt(r**2-(y-l)**2),y))
            if abs(100-l-x) <= r:
                if l <= y+sqrt(r**2-(x+l-100)**2) <= 100-l:
                    points.append((100-l,y+sqrt(r**2-(x+l-100)**2)))
                if l <= y-sqrt(r**2-(x+l-100)**2) <= 100-l:
                    points.append((100-l,y-sqrt(r**2-(x+l-100)**2)))
            if abs(100-l-y) <= r:
                if l <= x+sqrt(r**2-(100-l-y)**2) <= 100-l:
                    points.append((x+sqrt(r**2-(100-l-y)**2),y))
                if l <= x-sqrt(r**2-(100-l-y)**2) <= 100-l:
                    points.append((x-sqrt(r**2-(100-l-y)**2),y))
        for i in range(n): #円と円の交点をリストに入れる
            if n != 1 and i != n-1:
                for j in range(i+1, n):
                    p = crosscircle(cirs[i], cirs[j])
                    if p == ():
                        continue
                    for a in p:
                        if l <= a[0] <= 100-l and l <= a[1] <= 100-l:
                            points.append(a)
        points.append((l,l)) #正方形の四隅をリストに入れる
        points.append((100-l,l))
        points.append((l,100-l))
        points.append((100-l,100-l))
        for p in points: #リスト内の点が円の内部にないか判定する
            if not l <= p[0] <=100-l:
                continue
            if not l <= p[1] <=100-l:
                continue
            pok = True
            for c in cirs:
                if (p[0]-c[0])**2 + (p[1]-c[1])**2 <= (c[2]-eps)**2:
                    pok = False
                    break
            if pok:
                ok = True
                break
        if ok:
            L = R
        else:
            U = R
    print(R)
