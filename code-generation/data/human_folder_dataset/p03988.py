from collections import Counter
def solve(A):
    m = min(A)
    cnt = Counter(A)

    if cnt[m] > 2:
        return False

    if cnt[m] == 2:
        d = m-1
    else:
        d = m

    if max(A) > d+m:
        return False

    for i in range(1,d+1):
        if cnt[i+m] < 2:
            return False


    return True




if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    print('Possible' if solve(A) else 'Impossible')