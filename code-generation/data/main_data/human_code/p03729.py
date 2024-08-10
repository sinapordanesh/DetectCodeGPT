def iroha():
    a, b, c = input().split()
    
    s = a[len(a)-1]
    sshead = b[0]
    sstail = b[len(b)-1]
    sss = c[0]

    if s == sshead and sstail == sss:
        print("YES")
    else:
        print("NO")





if __name__ == "__main__":
    iroha()

