def iroha():
    a, b = map(int, input().split())

    if a == 2 or b == 2:
        print("No")
        return

    list = [4, 6, 9, 11]
    count = 0
    
    for x in list:
        if a == x or b == x:
            count += 1

    if count == 1:
        print("No")
        return
        
    print("Yes")


if __name__ == "__main__":
    iroha()

