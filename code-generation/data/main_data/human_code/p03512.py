import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit
def prime_table(N):
    is_prime = np.zeros(N, np.int64)
    is_prime[2:3] = 1
    is_prime[3::2] = 1
    for p in range(3, N, 2):
        if p * p >= N:
            break
        if is_prime[p]:
            is_prime[p * p::p + p] = 0
    return is_prime, np.where(is_prime)[0]

@njit((i8[:], ), cache=True)
def main(MX):
    _, primes = prime_table(300)
    primes_small = primes[primes < 18]
    primes_large = primes[primes > 18]
    M, X = MX[::2], MX[1::2]
    nums = np.array([1], np.int64)
    for p in primes_small:
        tmp = [1]
        while p * tmp[-1] < 300:
            tmp.append(p * tmp[-1])
        nums = np.ravel(
            nums.reshape(-1, 1) * np.array(tmp, np.int64).reshape(1, -1))

    U = nums[-1]

    ret = 0
    for n in nums:
        base = 0
        extra = np.zeros(300, np.int64)
        for i in range(len(M)):
            m, x = M[i], X[i]
            a = np.gcd(m, U)
            b = m // a
            if n % a != 0:
                continue
            if b == 1:
                base += x
            else:
                extra[b] += x
        score = base + np.sum(np.maximum(extra, 0))
        ret = max(ret, score)
    return ret

MX = np.array(read().split(), np.int64)[1:]

print(main(MX))