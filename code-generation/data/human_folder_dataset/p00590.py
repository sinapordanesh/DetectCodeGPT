import sys

def is_prime(x):
    if((x % 2 == 0 and x > 2) or x < 2):
        return 0
    elif(x <= 5):
        return 1
    a = 3
    while(a * a <= x):
        if(x % a == 0):
            return 0
        a += 2
    return 1

l = []
for i in sys.stdin:
    l.append(int(i))

for data in l:
    count = 0
    data1 = [i for i in range(1,data+1)]
    data2 = [i for i in range(data,0,-1)]
    for i in range(0,data):
        count += 1 if(is_prime(data1[i]) == 1 and is_prime(data2[i]) == 1) else 0
    print(count)
