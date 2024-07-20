def tax(n,r):
    return n*(100+r)//100

while True:
    x,y,s = map(int,input().strip().split(" "))
    if [x,y,s] == [0,0,0]:   #ｘは変更前税率、ｙは変更後税率、ｓは変更前税込み合計
        break
    S = []
    M = 0
    for i in range(1,s//2+1):
        for j in range(1,s-i+1):
            if  tax(i,x) + tax(j,x) == s:
                t = tax(i,y) + tax(j,y)
                if t > M:
                    M = t
    print(M)

