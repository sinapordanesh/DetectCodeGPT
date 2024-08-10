T, S, E, W, N, B = range(6)

class Dice:

    def __init__(self):
        self.state = list(range(6))

    def __eq__(self, dice):
        return self.state == dice.state

    def __gt__(self, dice):
        return self.state > dice.state

    def copy(self):
        dice = Dice()
        dice.state = [x for x in self.state]
        return dice

    def _turn(self, turn):
        k = self.state[turn[-1]]
        for i in range(4):
            self.state[turn[i]], k = k, self.state[turn[i]]

    def go_south(self):
        turn = [T, S, B, N]
        self._turn(turn)

    def go_north(self):
        turn = [N, B, S, T]
        self._turn(turn)

    def go_east(self):
        turn = [T, E, B, W]
        self._turn(turn)

    def go_west(self):
        turn = [T, W, B, E]
        self._turn(turn)

    def north(self):
        return self.state[N]

    def south(self):
        return self.state[S]

    def east(self):
        return self.state[E]

    def west(self):
        return self.state[W]

    def bottom(self):
        return self.state[B]

    def top(self):
        return self.state[T]

    def goto(self, n):
        func = [self.go_west, self.go_north, self.go_east, self.go_south]
        func[n]()

    def show(self):
        d = list("TSEWNB")
        for x, s in zip(d, self.state):
            print(x + " : {}".format(s))


import heapq

INF = 10**9
if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while True:
        dp = [[[[INF for _ in range(6)] for i in range(6)] for j in range(10)] for k in range(10)]
        h, w = map(int, input().split())
        if h == 0:
            break

        cost = [list(map(int, input().split())) for _ in range(h)]
        sy, sx = map(int, input().split())
        gy, gx = map(int, input().split())
        q = []
        dice = Dice()
        heapq.heappush(q, [0, sx, sy, dice])
        dp[sy][sx][dice.bottom()][dice.east()]

        ans = INF+1
        while q:
            c, x, y, dice = heapq.heappop(q)
            if x == gx and y == gy:
                ans = min(ans, c)
                continue
            if c >= ans:
                continue
            else:
                for i in range(4):
                    ddx, ddy = dx[i], dy[i]
                    if x + ddx >= w or x + ddx < 0 or y + ddy >= h or y + ddy < 0:
                        continue
                    else:
                        d = dice.copy()
                        d.goto(i)

                        new_cost = c + (d.bottom()+1)*cost[y+ddy][x+ddx]
                        if dp[y+ddy][x+ddx][d.bottom()][d.east()] > new_cost:
                            dp[y+ddy][x+ddx][d.bottom()][d.east()] = new_cost
                            heapq.heappush(q, [new_cost, x+ddx, y+ddy, d])
        print(ans)

