import sys


def main():
    h, w = map(int, sys.stdin.buffer.readline().split())
    n = int(sys.stdin.buffer.readline())
    a = list(map(int, sys.stdin.buffer.readline().split()))
    ans = [0]*(w*h)
    now = 0
    for i, x in enumerate(a):
        for j in range(x):
            ans[now + j] = i+1
        now += x

    for i in range(h):
        if i % 2:
            print(*reversed(ans[i*w:(i+1)*w]))
        else:
            print(*ans[i*w:(i+1)*w])


if __name__ == "__main__":
    main()
