M = int(input())

def tanri(a,y,nenri,tax):
    w = 0
    for i in range(y):
        w += int(a * nenri)
        a -= tax
    return a+w
def fukuri(a, y, nenri, tax):
    for i in range(y):
        a += int(a * nenri) - tax 
    return a

for i in range(M):
    A = int(input())
    Y = int(input())
    N = int(input())
    max_ = 0
    for i in range(N):
        t, nenri, tax = list(map(float,input().split()))
        max_ = max(max_, tanri(A,Y,nenri,tax) if t == 0 else fukuri(A,Y,nenri,tax))

    print(int(max_))