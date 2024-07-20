import math

def gcd_and_lcm():
    while True:
        try:
            a, b = map(int, input().split())
            gcd = math.gcd(a, b)
            lcm = abs(a*b) // gcd
            print(gcd, lcm)
        except EOFError:
            break

gcd_and_lcm()