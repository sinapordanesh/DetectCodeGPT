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

A,B,C,D,=LI()

if A + B > C + D:
    print("Left")
elif A + B == C + D:
    print("Balanced")
else:
    print("Right")