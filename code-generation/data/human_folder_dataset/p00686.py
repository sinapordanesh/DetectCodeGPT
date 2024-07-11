def numchange(boo):
    if boo:return 1
    else: return -1

while True:
    m,n = map(int,input().split())
    if m==0: break

    yaxis = 1
    xaxis = 1
    rotation = 0
    while True:
        lnr = input()
        if lnr == "STOP": break
        elif lnr == "RIGHT": rotation = (rotation+1)%4
        elif lnr == "LEFT": rotation = (rotation+3)%4
        else:
            movequeue = lnr.split()
            moveamount = int(movequeue[1]) * numchange((rotation//2)==0) * numchange(movequeue[0]=="FORWARD")
            if rotation%2==0:
                yaxis += moveamount
                if yaxis <= 0:
                    yaxis = 1
                elif yaxis > n:
                    yaxis = n
            else:
                xaxis += moveamount
                if xaxis <= 0:
                    xaxis = 1
                elif xaxis > m:
                    xaxis = m
    print(xaxis,yaxis)