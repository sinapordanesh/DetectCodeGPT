
def resolve():
    n = int(input())
    for i in range(1, 10):
        a = n // i
        if n % i == 0 and a < 10:
            print('Yes')
            return
    print('No')

if __name__ == "__main__":
    resolve()
