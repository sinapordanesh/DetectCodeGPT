import numpy as np

h,w = map(int,(input().split()))
s = [list(map(str,input())) for i in range(h)]
l = [[0]*(w+2) for i in range(h+2)]


def addFlag(i,j):
    for x in range(3):
        for y in range(3):
            if l[i+x][j+y] != '#':
                l[i+x][j+y] += 1
                
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            l[i+1][j+1] = '#'
            addFlag(i,j)

l = np.delete(l,[0,h+1],0)
l = np.delete(l,[0,w+1],1)


for i in l:
    ans = ''.join(map(str,i))
    print(ans)