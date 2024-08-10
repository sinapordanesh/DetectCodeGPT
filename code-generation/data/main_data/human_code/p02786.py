H = int(input())
attackcnt = 0
monstercnt = 1
def monster(h, m, a):
    if h == 1:
        return 0,0,a+m
    else:
        return monster(int((h/2)),2*m,a+m)
a, b, c = monster(H,monstercnt,attackcnt)
print(c)