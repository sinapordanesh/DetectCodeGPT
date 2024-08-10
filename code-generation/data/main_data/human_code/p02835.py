from sys import stdin, stdout

def print(x):
    stdout.write(str(x))

def solve():
    A = [int(x) for x in stdin.readline().split()]
    sum = 0
    for a in A:
        sum += a
    if sum < 22 :
        print("win")
    else:
        print("bust")

def main():
    solve()


if __name__ == "__main__":
    main()