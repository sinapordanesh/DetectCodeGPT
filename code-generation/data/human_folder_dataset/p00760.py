def day(y, m, d):
    days = 0
    days += (y-1)*195
    days += (y-1)//3*5
    days += (m-1)*19
    if y%3 == 0:
        days += (m-1)
    else:
        days += m//2
    days += (d-1)
    return days

def main():
    n = int(input())
    for _ in range(n):
        (y, m, d) = [int(x) for x in input().split()]
        print(day(1000,1,1) - day(y,m,d))

if __name__ == '__main__':
    main()