N=int(input())
T=input()
t=[]
tmp=0
sign="R"
for i in range(len(T)):
    if sign=="R":
        if T[i]=="R":
            tmp+=1
        else:
            if t and t[-1]!="S":
                t[-1]+=tmp
                sign="S"
                tmp=1
            else:
                t.append(tmp)
                tmp=1
                sign="S"
    else:
        if T[i]=="S":
            tmp+=1
        else:
            if tmp%2==1:
                t.append("S")
            tmp=1
            sign="R"

if sign=="R":
    if t and t[-1]!="S":
        t[-1]+=tmp
        sign="S"
        tmp=1
    else:
        t.append(tmp)
        tmp=1
        sign="S"
else:
    if tmp%2==1:
        t.append("S")
    tmp=1
    sign="R"

def dance(n,music):
    if n==0:
        return [0]
    res=[-1]*3**n
    for i in range(3):
        nmusic=[]
        val=i
        for j in range(len(music)):
            if music[j]!="S":
                tmp=music[j]//3
                if val+(music[j]%3)>=3:
                    tmp+=1
                if nmusic and nmusic[-1]!="S":
                    nmusic[-1]+=tmp
                elif tmp:
                    nmusic.append(tmp)
                val+=music[j]
                val%=3
            else:
                if nmusic and nmusic[-1]=="S":
                    nmusic.pop()
                else:
                    nmusic.append("S")
                val=(-val)%3
        rres=dance(n-1,nmusic)
        for j in range(3**(n-1)):
            res[3*j+i]=3*rres[j]+val
    return res


res=dance(N,t)
print(*res)