import sys
sys.setrecursionlimit(2147483647)
import math
from heapq import heappush, heappop, heapify

def solve(s):
  n = len(s)
  k = n
  for i in range(n-1):
    if s[i] != s[i+1]:
      k = min(k, max(i+1, n-i-1))
  return k

def main():
  s = input()
  ans = solve(s)
  print(ans)
  

if __name__=='__main__':
  main()