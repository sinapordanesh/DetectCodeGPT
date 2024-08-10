# A - Expired?
def main():
    x, a, b = map(int, input().split())

    if a >= b:
        print('delicious')
    elif b-a < x+1:
        print('safe')
    else:
        print('dangerous')



if __name__ ==  "__main__":
    main()