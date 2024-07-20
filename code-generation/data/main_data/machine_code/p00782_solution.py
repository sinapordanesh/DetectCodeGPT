def mobile_phone_coverage():
    import math
    n = int(input())
    count = 1
    while n != 0:
        antennas = []
        for _ in range(n):
            x, y, r = map(float, input().split())
            antennas.append((x, y, r))
        
        covered_points = set()
        for i in range(n):
            for j in range(i+1, n):
                x1, y1, r1 = antennas[i]
                x2, y2, r2 = antennas[j]
                min_x = max(x1 - r1, x2 - r2)
                max_x = min(x1 + r1, x2 + r2)
                min_y = max(y1 - r1, y2 - r2)
                max_y = min(y1 + r1, y2 + r2)
                for x in range(int(min_x), int(max_x) + 1):
                    for y in range(int(min_y), int(max_y) + 1):
                        covered_points.add((x, y))
        
        area = len(covered_points)
        print(f"{count} {area:.2f}")
        
        count += 1
        n = int(input())

mobile_phone_coverage()