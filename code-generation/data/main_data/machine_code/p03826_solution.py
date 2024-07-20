def compare_rectangle_areas(A, B, C, D):
    area1 = A * B
    area2 = C * D
    
    if area1 > area2:
        return area1
    elif area2 > area1:
        return area2
    else:
        return area1

A, B, C, D = map(int, input().split())
print(compare_rectangle_areas(A, B, C, D))