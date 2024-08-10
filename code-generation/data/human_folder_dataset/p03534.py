import math
s=input()
def kaibun(s):
    ls=len(s)

    if ls==1:
        print("YES")
        return
      
    ca,cb,cc=0,0,0
    l=[]
    for i in range(ls):
        if s[i]=="a":
            ca+=1
        if s[i]=="b":
            cb+=1
        if s[i]=="c":
            cc+=1
    l.append(ca)
    l.append(cb)
    l.append(cc)
    cnt_zero=0
    for j in l:
        if j==0:
            cnt_zero+=1
    if cnt_zero==2:
        print("NO")
        return

    elif cnt_zero==1:
        if ls==2:
            print("YES")
            return
        else:
            print("NO")
            return
          
    #cnt_zero=0のとき，つまりすべての文字が文字列に含まれるとき
    else:
        if ls==3 or ls==4:
            print("YES")
            return
        nmin=math.floor(ls/3.0)
        nmax=math.ceil(ls/3.0)
        nmax=int(nmax)
        nmin=int(nmin)
        #out=0
        for j in l:
            if j<nmin or nmax<j:
                print("NO")
                return

        print("YES")
        return
        
kaibun(s)