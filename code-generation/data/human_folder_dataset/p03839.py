from itertools import accumulate

def solve(A,K):

    opt = [0]+list(accumulate(a if a > 0 else 0 for a in A))
    plain = [0]+list(accumulate(A))

    def it():
        for i in range(len(A)-K+1):
            x = opt[i] + opt[-1] - opt[i+K]
            yield x
            yield x + plain[i+K] - plain[i]

    return max(it())


if __name__ == '__main__':
    N,K = map(int,input().split())
    A = list(map(int,input().split()))

    print(solve(A,K))