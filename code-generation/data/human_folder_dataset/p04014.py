from math import sqrt


def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n//b) + n % b


def divisors(P):
    res = set([])
    for i in range(1, P+1):
        if i**2 > P:
            break
        else:
            if P % i == 0:
                res.add(i)
                res.add(P//i)
    return res


def main():
    N = int(input())
    S = int(input())
    res = 10**18
    if N <= 10**6:
        for b in range(2, N+2):
            if f(b, N) == S:
                res = b
                break
        if res < 10**18:
            print(res)
        else:
            print(-1)
            return

    else:
        #N > 10**6
        for b in range(2, 10**6+2):
            if f(b, N) == S:
                res = b
                break
        if res < 10 ** 18:
            print(res)
            return
        else:
            if N < S:
                print(-1)
                return
            elif N == S:
                print(N+1)
                return
            else:
                div = divisors(N-S)
                for y in div:
                    sub_res = y + 1
                    if f(sub_res, N) == S:
                        res = min(res, sub_res)
                        
                if res < 10**18:
                    print(res)
                else:
                    print(-1)
                return

if __name__ == "__main__":
    main()
    

