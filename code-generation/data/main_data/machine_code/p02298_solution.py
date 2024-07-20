def is_convex():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
    is_neg = None
    for i in range(n):
        p1, p2, p3 = points[i], points[(i+1)%n], points[(i+2)%n]
        cp = cross_product(p1, p2, p3)
        if cp == 0:
            continue
        if is_neg is None:
            is_neg = cp < 0
        else:
            if (cp < 0) != is_neg:
                print("0")
                return
    print("1")

is_convex()