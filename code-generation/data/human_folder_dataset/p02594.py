import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
def main():
    x = int(input())
    if x >= 30:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()