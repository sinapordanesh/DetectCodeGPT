from sys import stdin
input = stdin.readline

def solve():

    N = int(input())
    a = [tuple(map(int,inp.split())) for inp in stdin.read().splitlines()]
    res = ((N+1)**2)*N//2-N*(N+1)*(2*N+1)//6
    for u,v in a:
        res -= min(u,v)*(N - max(u,v)+1)
    print(res)


if __name__ == '__main__':
    solve()