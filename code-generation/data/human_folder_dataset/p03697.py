def iroha():
    a, b = map(int, input().split())
    
    ans = a+b

    print(ans if ans < 10 else "error")



if __name__ == "__main__":
    iroha()

