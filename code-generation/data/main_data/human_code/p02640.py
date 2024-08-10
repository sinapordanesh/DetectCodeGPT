def main():
  X,Y = map(int,input().split())
  for x in range(101):
    for y in range(101):
      if x+y==X and 2*x+4*y==Y:
        return True
  return False

if __name__ == '__main__':
  print("Yes" if main() else "No")