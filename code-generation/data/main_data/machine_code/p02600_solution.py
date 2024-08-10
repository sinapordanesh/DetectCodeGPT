def atcoder_kyu_rating(X):
    if 400 <= X <= 599:
        return 8
    elif 600 <= X <= 799:
        return 7
    elif 800 <= X <= 999:
        return 6
    elif 1000 <= X <= 1199:
        return 5
    elif 1200 <= X <= 1399:
        return 4
    elif 1400 <= X <= 1599:
        return 3
    elif 1600 <= X <= 1799:
        return 2
    elif 1800 <= X <= 1999:
        return 1

X = int(input())
print(atcoder_kyu_rating(X))