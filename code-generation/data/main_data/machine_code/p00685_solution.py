def find_board_arrangements(rel_pos):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    def valid(arr):
        for i in range(16):
            for j in range(i + 1, 16):
                if (i // 4 - j // 4, i % 4 - j % 4) == rel_pos[0]:
                    if arr[i] != arr[j]:
                        return False
                if (i // 4 - j // 4, i % 4 - j % 4) == rel_pos[1]:
                    if arr[i] != arr[j]:
                        return False
                if (i // 4 - j // 4, i % 4 - j % 4) == rel_pos[2]:
                    if arr[i] != arr[j]:
                        return False
                if (i // 4 - j // 4, i % 4 - j % 4) == rel_pos[3]:
                    if arr[i] != arr[j]:
                        return False
        return True

    count = 0
    cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H']
    
    for a in range(1, 9):
        for b in range(1, 9):
            if b == a:
                continue
            for c in range(1, 9):
                if c == a or c == b:
                    continue
                for d in range(1, 9):
                    if d == a or d == b or d == c:
                        continue
                    arr = [cards[a-1], cards[b-1], cards[c-1], cards[d-1],
                           cards[d-1], cards[c-1], cards[b-1], cards[a-1],
                           cards[c-1], cards[d-1], cards[a-1], cards[b-1],
                           cards[b-1], cards[a-1], cards[d-1], cards[c-1]]
                    if valid(arr):
                        count += 1

    return count

# Sample Input
print(find_board_arrangements([-2, 1, -1, 1, 1, 1, 1, 2]))
print(find_board_arrangements([1, 0, 2, 1, 2, 2, 3, 3]))