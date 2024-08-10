ope = []
def plus(i,j,k):
    ope.append(('+',i,j,k))
def lt(i,j,k):
    ope.append(('<',i,j,k))

#assume a[0]+a[1] > 0
#a[3] = 1
plus(0,1,3)
lt(2,3,3)

#a[4] = A+1, a[5] = B+1
plus(0,3,4)
plus(1,3,5)

#a[1000] = 1, a[1001] = 2, a[1002] = 4, ..., a[1030] = 2**30
plus(1000,3,1000)
for i in range(30):
    plus(1000+i, 1000+i, 1000+i+1)

#a[2900] = x
#a[2901] = x + 2**i
#a[2000+i] = int(x + 2**i < A+1) : A_i
for i in range(29,-1,-1):
    plus(2900, 1000+i, 2901)
    lt(2901, 4, 2000+i)
    #x += a[2000+i] * 2**i
    lt(99, 2000+i, 2902)
    for j in range(i):
        plus(2902, 2902, 2902)
    plus(2900, 2902, 2900)

#a[3900] = x
#a[3901] = x + 2**i
#a[3000+i] = int(x + 2**i < B+1) : B_i
for i in range(29,-1,-1):
    plus(3900, 1000+i, 3901)
    lt(3901, 5, 3000+i)
    #x += a[3000+i] * 2**i
    lt(99, 3000+i, 3902)
    for _ in range(i):
        plus(3902, 3902, 3902)
    plus(3900, 3902, 3900)

# {A_0, ... A_29} * {B_0, ... B_29}
for a in range(30):
    for b in range(30):
        plus(2000+a, 3000+b, 4000)
        lt(3, 4000, 4001)
        for _ in range(a+b):
            plus(4001, 4001, 4001)
        plus(2, 4001, 2)

print(len(ope))
for row in ope:
    print(*row)