while True:
  d, w = map(int, input().split())
  if d == 0:break
  mp = [list(map(int, input().split())) for _ in range(d)]
  def solve():
    ans = 0
    for left in range(w - 1):
      for right in range(w - 1, left + 1, -1):
        for top in range(d - 1):
          for under in range(d - 1, top + 1, -1):
            frame_height = 10
            frame_height = min(frame_height, min(mp[top][left:right + 1]))
            frame_height = min(frame_height, min(mp[under][left:right + 1]))
            frame_height = min(frame_height, min(mp[i][left] for i in range(top, under)))
            frame_height = min(frame_height, min(mp[i][right] for i in range(top, under)))
            pond_height = 0
            pond_height = max(pond_height, max(max(mp[i][left + 1:right]) for i in range(top + 1, under)))
            if pond_height < frame_height:
              temp = frame_height * (under - top - 1) * (right - left - 1) - \
                    sum(sum(mp[i][left + 1:right]) for i in range(top + 1, under))
              ans = max(temp, ans)
    print(ans)
  
  solve()
