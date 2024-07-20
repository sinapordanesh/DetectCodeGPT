import bisect,collections,copy,heapq,itertools,math,string
import sys
def I():
    #1 line 1 int
     return int(sys.stdin.readline().rstrip())
def LI():
    #1 line n int
     return list(map(int,sys.stdin.readline().rstrip().split()))
def S():
    #1 line 1 string
     return sys.stdin.readline().rstrip()
def LS():
    #1 line n strings
     return list(sys.stdin.readline().rstrip().split())

A=S()

if A[0] == A[1] == A[2] or A[1] == A[2] == A[3]:
    print("Yes")
else:
    print("No")