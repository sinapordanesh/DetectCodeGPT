def can_buy_indefinitely(T, queries):
    result = []
    for query in queries:
        A, B, C, D = query
        if B > A:
            result.append("Yes")
        elif B <= A and B > C:
            result.append("No")
        else:
            x = (A - B) // (B - C)
            if (A - B) % (B - C) != 0:
                x += 1
            remaining_cans = B + x * (B - C)
            if remaining_cans > D:
                result.append("Yes")
            else:
                result.append("No")
    return result

T = 24
queries = [(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]

print("\n".join(can_buy_indefinitely(T, queries)) )