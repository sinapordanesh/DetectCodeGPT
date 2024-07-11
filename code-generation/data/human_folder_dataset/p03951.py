import sys
def input():
  return sys.stdin.readline().rstrip()

N=int(input())
s=input()
t=input()

def func():
  for i in range(N):
    if s[i:]==t[0:N-i]:
      return i+N
  return N*2

print(func())
