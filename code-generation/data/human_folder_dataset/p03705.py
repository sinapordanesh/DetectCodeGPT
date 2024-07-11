import sys

input = sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    ans = (B*(N-1) + A) - (A*(N-1)+B) + 1
    print(max(ans, 0))

if __name__ == '__main__':
    main()