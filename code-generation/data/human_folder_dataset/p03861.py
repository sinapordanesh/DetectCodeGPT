a,b,x = map(int,input().split())

def get(n):
    if n<0:
        return 0
    else:
        return n//x + 1
print(get(b)-get(a-1))