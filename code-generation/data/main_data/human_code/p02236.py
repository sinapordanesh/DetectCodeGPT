import sys
def input():
    return sys.stdin.readline()[:-1]
    
n = int(input())
p = [None] + list(map(float, input().split()))
q = list(map(float, input().split()))
T = [[500 for i in range(n+1)] for j in range(n+1)]

psum = [0] * (n+1)
qsum = [0] * (n+1)
qsum[0] = q[0]
for i in range(1,n+1):
    psum[i] = psum[i-1] + p[i]
    qsum[i] = qsum[i-1] + q[i]
    
for i in range(1,n+1):
    T[i][i] = p[i] + (q[i-1] + q[i])*2
    
for l in range(2,n+1):
    for i in range(1,n-l+1+1):
        val_list = [T[i][j] + T[j+2][i+l-1] for j in range(i,i+l-2)]
        val_list.append(T[i][i+l-2] + q[i+l-1])
        val_list.append(T[i+1][i+l-1] + q[i-1])
        if i-2>=0:
            w = psum[i+l-1]-psum[i-1] + qsum[i+l-1]-qsum[i-2]
        else:
            w = psum[i+l-1]-psum[i-1] + qsum[i+l-1]
        T[i][i+l-1] = min(val_list) + w
        
print(T[1][n])
