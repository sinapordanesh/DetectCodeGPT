import sys

def run():
    cars = []
    for _n in sys.stdin:
        n = int(_n)
        if n == 0:
            print(cars.pop())
        else:
            cars.append(n)

if __name__ == '__main__':
    run()


