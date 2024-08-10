# -*- coding: utf-8 -*-
"""
"""
import sys
from sys import stdin
from bisect import bisect_right
input = stdin.readline


def create_prime_list(limit):
    """ ??¨??????????????????????????§limit?????§????´???°?????????????±???????
    https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9
    """
    x = limit**0.5
    primes = []
    nums = [x for x in range(2, limit+1)]
    while nums[0]<=x:
        primes.append(nums[0])
        current_prime = nums[0]
        nums = [x for x in nums if x%current_prime != 0]
    primes.extend(nums)
    return primes


def main(args):
    # ??????????´???°?????????
    primes = create_prime_list(10000)
    twin_primes = []
    prev = primes[0]
    for p in primes[1:]:
        if p == prev + 2:
            twin_primes.append([prev, p])
        prev = p

    keys = [x[1] for x in twin_primes]
    while True:
        n = int(input())
        if n == 0:
            break
        r = bisect_right(keys, n)
        print(*twin_primes[r-1])


if __name__ == '__main__':
    main(sys.argv[1:])
    