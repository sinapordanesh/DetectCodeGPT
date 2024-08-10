def check_multiple_of_4():
    r, g, b = map(int, input().split())
    num = int(str(r) + str(g) + str(b))
    if num % 4 == 0:
        print("YES")
    else:
        print("NO")

check_multiple_of_4()