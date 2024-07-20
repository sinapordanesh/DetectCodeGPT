lst = input().split()

x = int(lst[0])
a = int(lst[1])
b = int(lst[2])

def distance(p):
   return abs(p - x)

if distance(a) < distance(b):
   print('A')
else:
   print('B')