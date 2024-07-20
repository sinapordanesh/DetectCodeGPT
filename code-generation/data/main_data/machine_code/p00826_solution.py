def monster_trap():
    while True:
        n = int(input())
        if n == 0:
            break
        lines = []
        for _ in range(n):
            x, y, x_, y_ = map(int, input().split())
            lines.append((x, y, x_, y_))

        intersection = False
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, x1_, y1_ = lines[i]
                x2, y2, x2_, y2_ = lines[j]
                if (x1 < 0 and x1_ > 0 and y2 < 0 and y2_ > 0) or (x2 < 0 and x2_ > 0 and y1 < 0 and y1_ > 0):
                    intersection = True
                    break
                if x1 == x1_ and x2 == x2_:
                    continue
                if x1 == x1_:
                    a2 = (y2_ - y2) / (x2_ - x2)
                    b2 = y2 - a2*x2
                    y = a2*x1 + b2
                    if y >= y1 and y <= y1_:
                        intersection = True
                        break
                elif x2 == x2_:
                    a1 = (y1_ - y1) / (x1_ - x1)
                    b1 = y1 - a1*x1
                    y = a1*x2 + b1
                    if y >= y2 and y <= y2_:
                        intersection = True
                        break
                else:
                    a1 = (y1_ - y1) / (x1_ - x1)
                    b1 = y1 - a1*x1
                    a2 = (y2_ - y2) / (x2_ - x2)
                    b2 = y2 - a2*x2
                    if a1 == a2:
                        continue
                    x = (b2 - b1) / (a1 - a2)
                    if x >= x1 and x <= x1_ and x >= x2 and x <= x2_:
                        intersection = True
                        break
            if intersection:
                break

        if intersection:
            print("no")
        else:
            print("yes")

monster_trap()