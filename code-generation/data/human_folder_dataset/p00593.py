import sys

def p(t):
    for l in t:
        for n in l:
            print("{0:>3}".format(n),end="")
        print("")

c = 0
for n in sys.stdin:
    n = int(n)

    if n == 0:
        break

    t = [ [ 0 for _ in range(n) ] for _ in range(n) ]

    c += 1
    print("Case {}:".format(c))

    x = 0
    y = 0
    up= True
    for i in range(1,n*n+1):
#        print("{} {}".format(x,y))
        t[y][x] = i
        if up:
            if y == 0:
                if x < n-1:
                    x += 1
                    up = False
                else:
                    y += 1
                    up = False
            else:
                if x < n-1:
                    x += 1
                    y -= 1
                else:
                    y += 1
                    up = False
                    
        else:
            if x == 0:
                if y < n-1:
                    y += 1
                    up = True
                else:
                    x += 1
                    up = True
            else:
                if y < n-1:
                    x -= 1
                    y += 1
                else:
                    x += 1
                    up = True

    p(t)

    