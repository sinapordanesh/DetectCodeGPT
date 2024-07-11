import sys, math

class Eratos(object):
    def __init__(self, N):
        self.N = N
        self._primes = {i:True for i in range(2, N+1)}

    def filter(self):
        end = self.N
        if self.N > 5:
            end = math.ceil(self.N**0.5) + 1
        for n in range(2, end):
            if not self._primes[n]:
                continue
            for x in range(n*2, self.N+1, n):
                if x in self._primes:
                    self._primes[x] = False
    
    def primes(self, x):
        return [k for k,v in self._primes.items() if v == True and k <= x]

def run():
    e = Eratos(999999)
    e.filter()
    for _n in sys.stdin:
        N = int(_n)
        print(len(e.primes(N)))

if __name__ == '__main__':
    run()


