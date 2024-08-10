def bubble_sort(cards):
    for i in range(len(cards)):
        for j in range(len(cards)-1, i, -1):
            if cards[j][1] < cards[j-1][1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]
    return cards

def selection_sort(cards):
    for i in range(len(cards)):
        mini = i
        for j in range(i, len(cards)):
            if cards[j][1] < cards[mini][1]:
                mini = j
        cards[i], cards[mini] = cards[mini], cards[i]
    return cards

N = int(input())
cards = input().split()
cards = [(c[0], int(c[1])) for c in cards]

bubble_result = bubble_sort(cards.copy())
bubble_stable = "Stable" if bubble_result == sorted(cards, key=lambda x: x[1]) else "Not stable"

selection_result = selection_sort(cards.copy())
selection_stable = "Stable" if selection_result == sorted(cards, key=lambda x: x[1]) else "Not stable"

print(" ".join(["".join(map(str, c)) for c in bubble_result]))
print(bubble_stable)
print(" ".join(["".join(map(str, c)) for c in selection_result]))
print(selection_stable)