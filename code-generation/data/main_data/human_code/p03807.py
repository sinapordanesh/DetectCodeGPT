def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]

def isEven(num):
  if num%2==0:
    return True
  else:
    return False

n=N()

a=list(map(int, input().split()))
even=0
for number in a:
  if isEven(number):
    even +=1
odd=n-even
if odd%2==1:
  print("NO")
else:
  print("YES")
