import math
def main():

    a, b, angleC = map(float, input().split())
    radC = angleC * math.pi / 180
    S = a * b * math.sin(radC) /2
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(radC))
    L = a + b + c
    h = S / a * 2
    print(S, L, h)

if __name__ == '__main__':
    main()

