"""http://mayokoex.hatenablog.com/entry/2015/06/11/124120を参照しました"""
"""三分探索、賢い"""
import sys
MI = 1e-6
def calc(x,y,b):
    res = 90000
    for bx,by,l in b:
        d = l**2-(x-bx)**2-(y-by)**2
        if d < res:
            res = d
    return res

def search_y(x,b):
    p = [-100,-33,33,100]
    for t in range(100):
        if abs(p[0]-p[3]) < MI:
            return (calc(x,p[0],b)+calc(x,p[3],b))/2
        l = calc(x,p[1],b)
        r = calc(x,p[2],b)
        if l < r:
            p[0] = p[1]
        else:
            p[3] = p[2]
        p[1] = (2*p[0]+p[3])/3
        p[2] = (p[0]+2*p[3])/3
    return (calc(x,p[0],b)+calc(x,p[3],b))/2

def search(b):
    p = [-100,-33,33,100]
    for t in range(100):
        if abs(p[0]-p[3]) < MI:
            return (search_y(p[0],b)+search_y(p[3],b))/2
        l = search_y(p[1],b)
        r = search_y(p[2],b)
        if l < r:
            p[0] = p[1]
        else:
            p[3] = p[2]
        p[1] = (2*p[0]+p[3])/3
        p[2] = (p[0]+2*p[3])/3
    return (search_y(p[0],b)+search_y(p[3],b))/2

def solve(n):
    b = [[int(x) for x in sys.stdin.readline().split()] for i in range(n)]
    ans = 0
    print(search(b)**0.5)

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    solve(n)

