from heapq import heappush, heappop
def main():
  n = int(input())
  que = []
  for i in range(n):
    lst = sorted(list(map(int, input().split()))[1:], reverse=True)[:i+1]
    heappush(que, lst[-1])
    for v in lst[:-1]:
      heappush(que, v)
      heappop(que)
  print(sum(que))
main()
