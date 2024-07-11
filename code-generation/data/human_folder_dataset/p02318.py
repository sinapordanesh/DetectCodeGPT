s1 = input()
s2 = input()
x = [[0 for i in range(len(s2))]for j in range(len(s1))]

def g(i,j):
    if i == 0 or j == 0:
        if s1[i] == s2[j]:
            x[i][j] = abs(i-j)
        else:
            if i == 0:
                x[i][j] = x[i][j-1] + 1
            else:
                x[i][j] = x[i-1][j] + 1
    elif s1[i] == s2[j]:
        x[i][j] = min(x[i-1][j-1],x[i][j-1]+1,x[i-1][j]+1)
    else:
        x[i][j] = min(x[i-1][j-1]+1,x[i][j-1]+1,x[i-1][j]+1)
        

for i in range(len(s1)):
    for j in range(len(s2)):
        g(i,j)

print(x[len(s1)-1][len(s2)-1])
