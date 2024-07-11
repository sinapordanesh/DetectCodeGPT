N = int(input())

def black_magic(n):
    d = {
        1: 1431655765,
        2: 858993459,
        4: 252645135,
        8: 16711935,
        16: 65535
    }
    n=(n&d[1])+((n>>1)&d[1])
    n=(n&d[2])+((n>>2)&d[2])
    n=(n&d[4])+((n>>4)&d[4])
    n=(n&d[8])+((n>>8)&d[8])
    n=(n&d[16])+((n>>16)&d[16])
    return n

while black_magic(N) - 1:
    N &= N-1
print(N)