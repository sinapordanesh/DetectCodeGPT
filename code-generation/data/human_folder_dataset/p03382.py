def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    A = set(map(int,input().split()))
    A = sorted(list(A))

    import bisect

    ans = A[-1]/2
    b = bisect.bisect_left(A,ans)

    if abs(ans-A[b])<abs(ans-A[max(0,b-1)]):
        print(A[-1],A[b])
    else:
        print(A[-1],A[b-1])

if __name__=='__main__':
    main()