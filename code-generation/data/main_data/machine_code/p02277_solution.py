def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x[1]:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

n = int(input())
cards = []
for _ in range(n):
    cards.append(input().split())

quicksort(cards, 0, n - 1)

stability = "Stable"
for i in range(n - 1):
    if cards[i][1] == cards[i + 1][1] and cards.index(cards[i]) > cards.index(cards[i + 1]):
        stability = "Not stable"
        break

print(stability)
for card in cards:
    print(card[0], card[1])