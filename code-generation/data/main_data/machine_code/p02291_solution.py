def reflection(p1, p2, q):
    def find_reflection(p1, p2, p):
        x1, y1 = p1
        x2, y2 = p2
        x, y = p
        
        dx, dy = x2 - x1, y2 - y1
        u = ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)
        
        x_reflection = x1 + u * dx
        y_reflection = y1 + u * dy
        
        return x_reflection, y_reflection
    
    for _ in range(q):
        p = tuple(map(int, input().split()))
        x_reflection, y_reflection = find_reflection(p1, p2, p)
        print(f"{x_reflection:.10f} {y_reflection:.10f}")