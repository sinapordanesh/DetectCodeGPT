def iroha():
    a, b, c = map(int, input().split())
    
    one = b - a
    two = c - b

    if one == two:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    iroha()

