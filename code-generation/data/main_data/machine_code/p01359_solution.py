def era_name(N, Q, data):
    for i in range(Q):
        query = int(input())
        found = False
        for era in data:
            if query >= era[2] and query <= era[3]:
                print(era[0], query-era[2]+1)
                found = True
                break
        if not found:
            print("Unknown")