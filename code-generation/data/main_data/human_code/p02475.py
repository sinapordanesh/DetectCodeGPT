import decimal
def main():
    a, b = map(int, input().split())
    decimal.getcontext().prec = len(str(a))
    print(int(decimal.Decimal(a)/decimal.Decimal(b)))


main()
