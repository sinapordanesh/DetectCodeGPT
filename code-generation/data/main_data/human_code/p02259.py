
N = int(input())
li = list(map(int,input().split()))

def BubbleSort(A):
    count = 0
    for i in range(len(A)):
        for j in reversed(range(i+1,len(A))):
            if A[j]<A[j-1]:
                #入れ替え
                a = A[j]
                b = A[j-1]
                A[j-1] = a
                A[j] = b
                count+=1
    return [A,count]

result = BubbleSort(li)    

print(" ".join(list(map(str,result[0]))))
print(result[1])
