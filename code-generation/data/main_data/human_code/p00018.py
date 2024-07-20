def sort(num):
   l = len(num)
   for i in range(0,l):
        for j in range(0,l-i-1):
            if num[j] < num[j+1]:
               temp = num[j]
               num[j] = num[j+1]
               num[j+1]=temp
   print(num[0],end='')
   for i in range(1,len(num)-1):
       print('',num[i],end='')
   print('',num[i+1])

a , b , c , d , e = map(int,input().split())
num = []
num.append(a)
num.append(b)
num.append(c)
num.append(d)
num.append(e)
sort(num)