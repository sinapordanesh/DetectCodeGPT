def find_integer(A, B):
    if (A + B) % 2 == 0:
        return (A + B) // 2
    else:
        return "IMPOSSIBLE"