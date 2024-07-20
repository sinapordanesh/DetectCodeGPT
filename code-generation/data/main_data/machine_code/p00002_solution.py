def digit_number():
    import sys

    for line in sys.stdin:
        a, b = map(int, line.split())
        digits = len(str(a + b))
        print(digits)

digit_number()