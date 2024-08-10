import sys

input = sys.stdin.readline

def main():
    N = int(input())
    for _ in range(N):
        a = int(input())
        if a%2 == 1:
            print('first')
            return
    print('second')
    
if __name__ == "__main__":
    main()
