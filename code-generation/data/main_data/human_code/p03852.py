import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    C = input()
    if C in ['a', 'i', 'u', 'e', 'o']:
        print('vowel')
    else:
        print('consonant')


if __name__ == '__main__':
    main()
