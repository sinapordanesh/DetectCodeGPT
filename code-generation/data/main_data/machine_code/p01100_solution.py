def gift_exchange_party(n, m, friendships):
    while n != 0 and m != 0:
        min_gifts = 0
        max_gifts = 0
        
        for i in range(1, n+1):
            count = 0
            for j in range(m):
                if i == friendships[j][0]:
                    count += 1
                if i == friendships[j][1]:
                    count -= 1
            if count < min_gifts:
                min_gifts = count
            if count > max_gifts:
                max_gifts = count
        
        print(min_gifts*(-1), max_gifts)
        
        n, m, *friendships = map(int, input().split())