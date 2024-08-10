x, t = list(map(int, input().split()))

def answer(x: int, t: int) -> int:
    if x > t:
        return x - t
    else:
        return 0

print(answer(x, t))