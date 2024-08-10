# from sys import stdin
# input = stdin.readline


def solve():
    s = input()
    t = input()
    res = 0
    for a,b in zip(s,t):
        if a != b:
            res += 1
    print(res)







if __name__ == '__main__':
    solve()