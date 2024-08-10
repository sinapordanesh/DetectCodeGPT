N = int(input())

def aa(s, n, t):
    if n == N:
        print(s)
        return
    for i in range(t):
        aa(s+chr(97+i), n+1, t)
    aa(s+chr(97+t), n+1, t+1)
    return


aa("a", 1, 1)