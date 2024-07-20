import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    K = int(readline())
    a = 0
    ans = 0
    for _ in range(K+1):
        a = 10*a+7
        a %= K
        ans += 1
        if a%K == 0:
            break

    if ans == K+1: 
        print(-1)
    else:
        print(ans)
if __name__ == '__main__':
    main()
