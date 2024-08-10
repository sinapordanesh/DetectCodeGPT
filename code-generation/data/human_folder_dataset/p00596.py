import sys

def subset(line):
    l = line.strip().split(" ")
    a = list(map(int, l))
    xy = list(map(lambda x: [x // 10, x % 10], a))
    dominos = [[2 if [x, y] in xy and x == y else \
                1 if [x, y] in xy else \
                1 if [y, x] in xy else 0 \
                for x in range(0, 7)] for y in range(0, 7)] 
    digits = []
    for i in xy:
        digits.extend(i)
    digits = list(set(digits))
    digits.sort()
    return digits, dominos

def add_matrix(a, b):
    c = [[a[j][i] + b[j][i] for i in range(0, 7)] for j in range(0, 7)]
    return c

def mul_matrix(a, b):
    c = [[0 for i in range(0, 7)] for j in range(0, 7)]
    for j in range(0, 7):
        for i in range(0, 7):
            for k in range(0, 7):
                c[j][i] += a[j][k] * b[k][i]
    return c
                
def is_connected(d, g):
    a = g[:]
    z = [[0 for i in range(0, 7)] for j in range(0, 7)]
    b = a
    for i in range(0, 7):
        z = add_matrix(z, b)
        b = mul_matrix(b, a)
    zeros = 0
    for i in d:
        if z[d[0]][i] == 0:
            zeros += 1
    return zeros == 0
        
lno = 0
for line in sys.stdin:
    lno += 1
    if lno == 1:
        n = int(line)
    else:
        digits, dominos = subset(line)
        if not is_connected(digits, dominos):
            print("No")
        else:
            order = [sum(dominos[i]) for i in range(0, 7)]
            odd = 0
            for i in digits:
                if order[i] % 2 != 0:
                    odd += 1
            if odd <= 2:
                print("Yes")
            else:
                print("No")
        lno = 0
