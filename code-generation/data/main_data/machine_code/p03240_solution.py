def find_pyramid_center_and_height():
    N = int(input())
    points = []
    for _ in range(N):
        x, y, h = map(int, input().split())
        points.append((x, y, h))
    
    for C_X in range(101):
        for C_Y in range(101):
            for point in points:
                x, y, h = point
                if h > 0:
                    H = h + abs(x - C_X) + abs(y - C_Y)
                    break
            
            valid = True
            for point in points:
                x, y, h = point
                if max(H - abs(x - C_X) - abs(y - C_Y), 0) != h:
                    valid = False
                    break
            
            if valid:
                return f"{C_X} {C_Y} {H}"

print(find_pyramid_center_and_height())