def mapt(fn, *args):
    return tuple(map(fn, *args))
  

def Vector(line):
    return mapt(Atom, line.split(" "))


def Atom(segment):
    try:
        return float(segment)
    except ValueError:
        try:
            int(segment)
        except ValueError:
            return segment

def main():
    n = int(input())
    data = [Vector(input()) for _ in range(n)]
    total = 0
    for amount, currency in data:
        if currency == "JPY":
            total += amount
        else:
            total += amount * 380000
    print(total)

main()