def solve():
    from collections import deque
    from sys import stdin
    f_i = stdin
    
    ans = []
    while True:
        m, c, n = map(int, f_i.readline().split())
        if m == 0:
            break
        
        book_pos = dict()
        studens = deque()
        shelf = m + 1
        
        for i in range(n):
            k = int(f_i.readline())
            books = deque(map(int, f_i.readline().split()))
            for b in books:
                book_pos[b] = shelf
            studens.append(books)
        
        desk = [0] * (m + 1) # number of books on the desk
        D1 = deque()
        cost = 0
        
        while studens:
            s = studens.popleft()
            b = s.popleft()
            
            # get the book
            pos = book_pos[b]
            cost += pos
            if pos == 1:
                D1.remove(b)
            elif pos != shelf:
                desk[pos] -= 1
            
            if len(D1) == c:
                for i, cnt in enumerate(desk[2:], start=2):
                    if cnt < c:
                        # put the book on the i-th desk
                        desk[i] += 1
                        book_pos[b] = i
                        cost += i
                        b_pos = i
                        break
                else:
                    # put the book on the shelf
                    book_pos[b] = shelf
                    cost += shelf
                    b_pos = shelf
                    
                # get the unrequested book on D1
                unrequested = D1.popleft()
                cost += 1
                
                if b_pos == shelf:
                    # put the unrequested book to the shelf
                    book_pos[unrequested] = shelf
                    cost += shelf
                else:
                    for i, cnt in enumerate(desk[b_pos:], start=b_pos):
                        if cnt < c:
                            # put the unrequested book to i-th desk
                            desk[i] += 1
                            book_pos[unrequested] = i
                            cost += i
                            break
                    else:
                        # put the unrequested book to the shelf
                        book_pos[unrequested] = shelf
                        cost += shelf
                
                # take the book from the temporary place to D1
                if b_pos != shelf:
                    desk[b_pos] -= 1
                D1.append(b)
                book_pos[b] = 1
                cost += (b_pos + 1)
            else:
                # return the book to D1
                D1.append(b)
                book_pos[b] = 1
                cost += 1
            
            if s:
                studens.append(s)
        
        ans.append(cost)
    
    print('\n'.join(map(str, ans)))

solve()
