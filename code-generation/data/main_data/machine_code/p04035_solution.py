def untie_knots(N, L, ropes):
    if any(rope >= L for rope in ropes):
        print("Possible")
        for i in range(N-1):
            print(i+1)
    else:
        print("Impossible")