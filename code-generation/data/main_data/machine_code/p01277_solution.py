def check_symmetry():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            symmetry_x = 2*x2 - x1
            symmetry_y = 2*y2 - y1
            
            if [symmetry_x, symmetry_y] not in points:
                print("No")
                return
    
    print("Yes")