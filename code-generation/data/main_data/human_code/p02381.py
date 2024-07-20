import math
def main():

    while True:
        n = int(input())
        if n == 0:
            break
        else:
            data = list(map(float, input().split()))
            avg = sum(data) / n
            square = 0
            for i in range(n):
                square += data[i]**2
            print(math.sqrt((square / n - avg**2)))
            
if __name__ == '__main__':
    main()

