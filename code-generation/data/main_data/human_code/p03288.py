def main():
    n = int(input())
    if n < 1200:
        print("ABC")
    elif 1200 <= n < 2800:
        print("ARC")
    else:
        print("AGC")


main()