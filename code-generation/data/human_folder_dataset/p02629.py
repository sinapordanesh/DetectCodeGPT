def ri():
    return int(input())


def rii():
    return [int(v) for v in input().split()]


def solve():
    N = ri()
    ans = ""
    
    while N:
        N, r = divmod(N - 1, 26)
        ans  = chr(ord("a") + r) + ans
        
    print(ans)

if __name__ == "__main__":
    solve()