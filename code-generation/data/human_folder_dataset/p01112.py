from itertools import combinations as comb

def main():
  while True:
    n = int(input())
    if n ==0:break
    m = int(input())
    result = [[None] * n for _ in range(n)]
    for _ in range(m):
      x, y = map(int, input().split())
      x -= 1
      y -= 1
      result[x][y] = True
      result[y][x] = False

    t_count = [lst.count(True) for lst in result]
    
    empty_index = [[] for _ in range(n)]
    empty_nums = [0] * n
    for i in range(n):
      for j in range(i + 1, n):
        if result[i][j] == None:
          empty_index[i].append(j)
          empty_nums[i] += 1

    limit = n // 2
    def search(x, t_count):
      if x == n:return 1
      choice_num = limit - t_count[x]
      if choice_num < 0 or choice_num > empty_nums[x]:return 0
      rest_num = empty_nums[x] - choice_num
      ret = 0
      for inds in comb(empty_index[x], rest_num):
        new_count = t_count[:]
        for ind in inds:
          new_count[ind] += 1
        ret += search(x + 1, new_count)
 
      return ret

    print(search(0, t_count))

main()
