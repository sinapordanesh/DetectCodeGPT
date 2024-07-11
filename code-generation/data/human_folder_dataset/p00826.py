def string_to_complex(s):
    a, b, c, d = map(int, s.split())
    return (a + b * 1j, c + d * 1j)

def dot(c1, c2):
    return c1.real * c2.real + c1.imag * c2.imag

def cross(c1, c2):
    return c1.real * c2.imag - c1.imag * c2.real

def cross_point(p1, p2, p3, p4):
    crs1 = cross(p2 - p1, p3 - p1)
    crs2 = cross(p2 - p1, p4 - p1)
    if crs1 == 0 and crs2 == 0:
        if p1 == p3 or p1 == p4:
            return p1
        elif p2 == p3 or p2 == p4:
            return p2
        else:
            return None
    crs3 = cross(p4 - p3, p1 - p3)
    crs4 = cross(p4 - p3, p2 - p3)
    if crs1 * crs2 <= 0 and crs3 * crs4 <= 0:
        base = p4 - p3
        hypo1 = p1 - p3
        hypo2 = p2 - p3
        d1 = abs(cross(base, hypo1)) / abs(base)
        d2 = abs(cross(base, hypo2)) / abs(base)
        return p1 + d1 / (d1 + d2) * (p2 - p1)
    else:
        return None

def contain(polygon):
    flag = False
    for a, b in zip(polygon[0:], polygon[1:] + [polygon[0]]):
        if a.imag > b.imag:
            a, b = b, a
        if a.imag <= 0 and b.imag > 0 and cross(a, b) > 0:
            flag = not flag
    return flag

def solve():
    def dfs_contain(goal, edges, cross_points):
        cur_edge = edges[-1]
        for next_edge, next_cp in adj_edge[cur_edge]:
            if next_edge == goal:
                if contain(cross_points + [next_cp]):
                    break
            elif next_edge not in edges and unchecked[next_edge] and DP[next_edge]:
                edges.append(next_edge)
                cross_points.append(next_cp)
                if dfs_contain(goal, edges, cross_points):
                    break
                e = edges.pop()
                DP[e] = False
                cross_points.pop()
        else:
            return False
        return True
            
    from sys import stdin
    lines = stdin.readlines()
    
    from itertools import combinations
    
    while True:
        n = int(lines[0])
        if n == 0:
            break
        
        edges = enumerate(map(string_to_complex, lines[1:1+n]))
        adj_edge = [[] for i in range(n)]
        
        for e1, e2 in combinations(edges, 2):
            n1, t1 = e1
            n2, t2 = e2
            cp = cross_point(*t1, *t2)
            if cp:
                adj_edge[n1].append((n2, cp))
                adj_edge[n2].append((n1, cp))
        
        flag = True
        while flag:
            for i, ae in enumerate(adj_edge):
                if len(ae) == 1:
                    ne, cp = ae.pop()
                    adj_edge[ne].remove((i, cp))
                    break
            else:
                flag = False
        
        unchecked = [True] * n
        
        for e in range(n):
            unchecked[e] = False
            DP = [True] * n
            if dfs_contain(e, [e], []):
                print('yes')
                break
        else:
            print('no')
        
        del lines[:1+n]

solve()
