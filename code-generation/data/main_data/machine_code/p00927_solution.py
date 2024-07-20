import math

def space_golf(d, n, b, obstacles):
    def check_valid(v_ix, v_iy):
        nonlocal d, b, obstacles
        
        for i in range(1, len(obstacles)):
            x1, h1 = obstacles[i-1]
            x2, h2 = obstacles[i]
            
            v = (2 * v_ix * v_iy) / math.sqrt(1 + ((g * x2) / (v_ix * v_iy))**2)
            if v < h1 or v < h2:
                return False
        
        x_end = d
        v = (2 * v_ix * v_iy) / math.sqrt(1 + ((g * x_end) / (v_ix * v_iy))**2)
        if v < obstacles[-1][1]:
            return False
        
        return True
    
    g = 1.0
    low = 0.0
    high = 1000.0
    
    while high - low > 0.0001:
        mid = (low + high) / 2
        
        v_ix = mid
        v_iy = mid
        
        if check_valid(v_ix, v_iy):
            high = mid
        else:
            low = mid
    
    return round(mid, 5)