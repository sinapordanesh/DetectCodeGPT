month,day = map(int,input().split())

def takahashi(m,d):
    if d//10<2:
        return False
    if d%10<2:
        return False

    return (d//10) * (d%10) == m

cnt=0
for m in range(1,month+1):
    for d in range(1,day+1):
        if takahashi(m,d):
            cnt+=1
print(cnt)
