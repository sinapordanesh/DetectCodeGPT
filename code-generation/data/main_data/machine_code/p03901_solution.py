import sys

def main():
    x, p = map(int, sys.stdin.readline().split())
    
    if p == 100:
        print("1.0000000")
    else:
        p /= 100
        answer = p * x + (1 - p) * x * (1 - p) / (2 * p)
        print("{:.7f}".format(answer))

if __name__ == "__main__":
    main()