def main():
    n = int(input())
    a = set([int(a) for a in input().split()])
    m = int(input())
    b = set([int(a) for a in input().split()])

    c = a.symmetric_difference(b)
    sorted_c = sorted(c)
    for i in sorted_c:
        print(i)
main()

