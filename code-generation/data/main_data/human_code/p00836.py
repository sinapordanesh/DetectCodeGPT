from collections import defaultdict


class Primes():
    def __init__(self, N):
        self.N = N
        self.prime = {i for i in range(2, self.N+1)}
        for i in range(2, self.N+1):
            if i in self.prime:
                for j in range(i*2, self.N+1, i):
                    if j in self.prime:
                        self.prime.remove(j)

    def show_primes(self):
        return sorted(list(self.prime))


def main():
    D = defaultdict(int)
    P = Primes(10000)
    prime = P.show_primes()
    prime.insert(0, 0)
    L = len(prime)
    for i in range(1, L):
        prime[i] += prime[i-1]
    # prime[i]:=Primeの0番目からi番目までの素数の累積合計(i==0の時は0)
    for i in range(L):
        for j in range(i+1, L):
            D[prime[j]-prime[i]] += 1
            # 全ての10000以下の素数からなす素数列の部分列の総和を求めている
    # L=10**3より全体計算量はL**2=10**6で十分早い
    V = 1
    while V != 0:
        V = int(input())
        if V==0:
            continue
        print(D[V])
    return


if __name__ == "__main__":
    main()
