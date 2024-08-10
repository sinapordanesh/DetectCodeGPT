# A - RGB Cards
def main():
    r, g, b = input().split()
    rgb = r+g+b

    if int(rgb) % 4 == 0:
        print('YES')
    else:
        print('NO')



if __name__ ==  "__main__":
    main()