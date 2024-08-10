
def find_favorite_integer():
    low = 1
    high = 10**9

    while low < high:
        mid = (low + high) // 2
        print("? " + str(mid))
        ans = input().strip()

        if ans == "N":
            high = mid
        else:
            low = mid + 1

    print("! " + str(low))

find_favorite_integer()