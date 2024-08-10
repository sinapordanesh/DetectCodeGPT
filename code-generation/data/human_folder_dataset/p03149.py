import itertools
def main():
    num = list(map(int, input().split()))
    num.sort()

    if num[0] == 1 and num[1] == 4 and num[2] == 7 and num[3] == 9:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()