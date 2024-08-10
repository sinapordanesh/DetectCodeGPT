import sys
import re
import queue
import collections
from math import ceil, floor, sqrt, pi, factorial, gcd
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
	N,X,M=i_map()

	Y = X

	went_array = []
	for i in range(0,M):
		went_array.append(-1)

	loop_flag = False
	first = -1
	second = -1
	value = -1
	for i in range(0,N):

		if(went_array[Y] != -1):
			loop_flag = True
			first = went_array[Y]
			second = i
			value = Y
			break

		went_array[Y] = i
		Y = (Y*Y) % M

	if(loop_flag == False):
		Z = X
		sum = 0

		for i in range(0,N):
			sum += Z
			Z = (Z*Z)%M

		print(sum)

	else:
		Z = X
		sum1 = 0
		for i in range(0,first):
			sum1 += Z
			Z = (Z*Z)%M

		Z = value
		cum = []
		cum.append(Z)
		Z = (Z*Z) %M
		for i in range(1,second-first):
			cum.append(cum[i-1]+Z)
			Z = (Z*Z) %M

		sum2 = ((N-first)//(second-first))*cum[second-first-1]

		if((N-first)%(second-first) == 0):
			print(sum1 + sum2)
		else:
			sum3 = cum[((N-first)%(second-first)-1)]
			print(sum1 + sum2 + sum3)


	return

if __name__ == '__main__':
	main()