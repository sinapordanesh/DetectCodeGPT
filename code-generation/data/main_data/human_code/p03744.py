# なんだか釈然としていないが解説の通りに
from collections import deque
import sys

def MI(): return map(int, sys.stdin.readline().split())

class water:
    def __init__(self, t, v):
        self.v = v
        self.tv = v * t

    def __le__(self, other):
        return self.v * other.tv - self.tv * other.v >= 0

    def __isub__(self, other):
        t = self.tv / self.v
        self.v -= other
        self.tv = t * self.v
        return self

    def __iadd__(self, other):
        self.v+=other.v
        self.tv+=other.tv
        return self

def main():
    n, l = MI()
    dam = deque()
    t, v = MI()
    print(t)
    dam.append(water(t, v))
    # stvはtvの合計（vがlのときのvt）
    stv = t * v
    for _ in range(n-1):
        t, v = MI()
        # 朝に水をもらう
        dam.appendleft(water(t, v))
        over = v
        stv += t * v
        # 増えた分の水を古い方から捨てる
        # ベクトルごと削除できるもの
        while dam[-1].v <= over:
            w = dam.pop()
            over -= w.v
            stv -= w.tv
        # 最後のはみ出しているベクトルは縮める
        stv -= dam[-1].tv  # 一度合計から取り出して
        dam[-1] -= over  # 縮めて
        stv += dam[-1].tv  # 元に戻す
        # その日の水温を出力
        print(stv / l)
        # グラフの左側が凹んでいたらベクトルを合成して凸に直す
        while len(dam)>1 and dam[0] <= dam[1]:
            w = dam.popleft()
            dam[0] += w

main()
