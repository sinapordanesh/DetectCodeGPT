def get10(x):
    ans =0
    alphabet = {'m':1000,'c':100,'x':10,'i':1}
    i =0
    while i < len(x):
        if not x[i] in alphabet:
            ans += int(x[i])*alphabet[x[i+1]]
            i +=2
        elif x[i] in alphabet:
            ans +=alphabet[x[i]]
            i+=1
    return ans

def getN(x):
    ans =[]
    temp = x
    while temp !=0:
        if temp//1000:
            if temp//1000 == 1: ans.append('m')
            else:
                ans.append(str(temp//1000)+'m')
            temp = temp%1000
        elif temp//100:
            if temp//100 == 1: ans.append('c')
            else:
                ans.append(str(temp//100)+'c')
            temp = temp%100
        elif temp//10:
            if temp//10 == 1: ans.append('x')
            else:
                ans.append(str(temp//10)+'x')
            temp = temp%10
        else:
            if temp == 1:ans.append('i')
            elif temp >0:
                ans.append(str(temp)+'i')
            temp = temp//10
        
    
    return  ''.join(ans)



n = int(input())
for _ in range(n):
    x,y = input().split(' ')
    temp =get10(x) + get10(y)
    print(getN(temp))


