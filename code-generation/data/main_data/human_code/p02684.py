import sys
import re
import queue
import collections
import math
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []


def main():
	N,K = i_map()
	A = i_list()

	for i in range(0,len(A)):
		A[i] = A[i] - 1

	lengthA = math.ceil(math.log2(K))

	next = [[0 for _ in range(N)] for _ in range(lengthA)]
	
	for i in range(0,N):
		next[0][i] = A[(i)%(N)]

	for i in range(1,lengthA):
		for j in range(0,N):
			next[i][j] = next[i-1][next[i-1][j]]

	current = 0

	for i in range(0,lengthA):
		if((1 << i) & K):
			current = next[i][current]

	print(current+1)

	return

if __name__ == '__main__':
	main()