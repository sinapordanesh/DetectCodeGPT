def multiple_of_9(N):
    return "Yes" if sum(int(x) for x in str(N)) % 9 == 0 else "No"