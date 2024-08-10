def main():
    n = int(input())
    a, b = "Hello ", "World"
    if n == 2:
        a, b = [int(input()) for _ in range(n)]
    print(a+b)


main()