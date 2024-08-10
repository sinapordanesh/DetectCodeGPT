def Is_ToPut(p,w,k):
    count =1
    temp =p
    for i in w:
        if temp >= i:
            temp -=i
        elif i > p :
            return 0
        else:     
            count +=1
            temp =p-i
    if count <= k:return 1
    else:return 0

n,k = list(map(int,input().split(' ')))
w =[]
for _ in range(n):
    w.append(int(input()))
ans =100000*10000
left = 0
right = 100000*10000
while left < right:
    p = (left+right)//2
    if Is_ToPut(p,w,k):
        if ans > p:ans =p
        right=p
    else:
        left = p +1
print(ans)
        
