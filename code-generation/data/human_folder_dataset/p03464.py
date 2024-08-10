# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, A):
    mx = 2
    mn = 2
    for a in reversed(A):
        mx = (mx // a + 1) * a - 1
        mn = (mn + a - 1) // a * a
        if mn > mx:
            print(-1)
            return
    print(mn, mx)

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
