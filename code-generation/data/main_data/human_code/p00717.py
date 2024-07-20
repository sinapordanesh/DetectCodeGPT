import sys

def spin(x):
    result=[]
    for i in x:
        result.append([-1*i[1],i[0]])
    return result
def rev(x):
    y=x.copy()
    y.reverse()
    a=y[0][0]
    b=y[0][1]
    for i in y:
        i[0]-=a
        i[1]-=b
    return y

def check(x):
    if x==line_original or spin(x)==line_original or spin(spin(x))==line_original or spin(spin(spin(x)))==line_original:
        return True
    else:
        return False



while True:
    n=int(input())
    if n==0:
        sys.exit()

    m=int(input())
    line_original=[[0,0]]
    a,b=[int(i) for i in input().split(" ")]
    for count in range(m-1):
        p,q=[int(i) for i in input().split(" ")]
        line_original.append([p-a,q-b])
    line_list=[]
    for loop in range(n):
        m=int(input())
        line=[[0,0]]
        a,b=[int(i) for i in input().split(" ")]
        for count in range(m-1):
            p,q=[int(i) for i in input().split(" ")]
            line.append([p-a,q-b])
        line_list.append(line)

    for i in range(n):
        if (check(line_list[i])==True) or (check(rev(line_list[i]))==True):
            print(i+1)
    print("+++++")
    