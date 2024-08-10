def _get_distance(c1, c2):
    return ((c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5 - c1[0] - c2[0]

from itertools import combinations

def _get_min_distance(circles):
    min_d = float("inf")
    for c1, c2 in combinations(circles, 2):
        min_d = min(min_d, _get_distance(c1, c2))
    return min_d

def closest_pair_distance(circles, axis =1):
    # axis: x; 1, y; 2
    n = len(circles)
    if n <= 3:
        return _get_min_distance(circles)
    else:
        mid = n // 2
        r, x, y = zip(*circles)
        
        if len(set(x)) > len(set(y)):
            if axis == 2:
                circles.sort(key = lambda c: c[1] - c[0])
            axis1 = 1
            axis2 = 2
        else:
            if axis == 1:
                circles.sort(key = lambda c: c[2] - c[0])
            axis1 = 2
            axis2 = 1
        
        A_circles = circles[:mid]
        B_circles = circles[mid:]
        
        d_Amin = closest_pair_distance(A_circles.copy(), axis1)
        d_Bmin = closest_pair_distance(B_circles.copy(), axis1)
        dist = min(d_Amin, d_Bmin)
        min_d = dist
        
        A_circles.sort(key = lambda c: c[axis] + c[0])
        B_edge = B_circles[0][axis1] - B_circles[0][0]
        for ac in A_circles[::-1]:
            ac_r = ac[0]
            ac_edge = ac[axis1] + ac_r
            if B_edge - ac_edge >= dist:
                break
            for bc in B_circles:
                bc_r = bc[0]
                if bc[axis1] - bc_r - ac_edge >= dist:
                    break
                if abs(ac[axis2] - bc[axis2]) - ac_r - bc_r < dist:
                    min_d = min(min_d, _get_distance(ac, bc))
        return min_d

# solve
def solve():
    import sys
    input_lines = sys.stdin.readlines()
    while True:
        N = int(input_lines[0])
        if N == 0:
            break
        circles = [tuple(map(float, l.split())) for l in input_lines[1:N+1]]
        print('{:.8f}'.format(closest_pair_distance(circles)))
        del input_lines[:N+1]

solve()
