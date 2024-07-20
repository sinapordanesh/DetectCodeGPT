def main():
  while True:
    w, h = map(int, input().split())
    if w == 0:
      break
  
    mp = [[-1] + list(map(int, input().split())) + [-1] for _ in range(h)]
    mp.insert(0, [-1] * (w + 2))
    mp.append([-1] * (w + 2))
  
    for y in range(1, h + 1):
      for x in range(1, w + 1):
        if mp[y][x] == 2:
          start = (x, y)
        if mp[y][x] == 3:
          goal = (x, y)
  
    vec = ((0, -1), (0, 1), (-1, 0), (1, 0))
    
    def search(now, goal, num):
      if num <= 0:
        return -1
      bx, by = now
      ret = -1
      for dx, dy in vec:
        if mp[by + dy][bx + dx] in (-1, 1):
          continue
        nx, ny = bx, by
        while mp[ny + dy][nx + dx] not in (-1, 1):
          nx += dx
          ny += dy
          if (nx, ny) == goal:
            ret = max(ret, num - 1)
            break
        else:
          if mp[ny + dy][nx + dx] == 1:
            mp[ny + dy][nx + dx] = 0
            ret = max(ret, search((nx, ny), goal, num - 1))
            mp[ny + dy][nx + dx] = 1
  
      return ret
  
    
    score = search(start, goal, 10)
    if score == -1:
      print(-1)
    else:
      print(10 - score)

main()
