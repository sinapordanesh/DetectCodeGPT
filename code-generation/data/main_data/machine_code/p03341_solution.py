def min_people_to_change_directions(N, S):
    count_E = S.count('E')
    min_changes = min(count_E, N - count_E)
    return min_changes

N = int(input())
S = input().strip()
print(min_people_to_change_directions(N, S))