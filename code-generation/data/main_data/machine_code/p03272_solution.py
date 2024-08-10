def find_matching_car(N, i):
    return N - i + 1

N, i = map(int, input().split())
print(find_matching_car(N, i))