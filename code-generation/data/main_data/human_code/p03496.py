
def main():
    N = int(input())
    a = list(map(int, input().split()))

    amax = max(a)
    amin = min(a)
    OP = []
    if abs(amax) >= abs(amin):
        idx = a.index(amax) + 1
        OP += [(idx, i) for i in range(1,N+1)]
        OP += [(i, i+1) for i in range(1, N)]
    else:
        idx = a.index(amin) + 1
        OP += [(idx, i) for i in range(1,N+1)]
        OP += [(i+1, i) for i in reversed(range(1,N))]
    
    print(len(OP))
    for op in OP: print(*op)

main()
