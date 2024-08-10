def book_replacement(m, c, n, requests):
    total_cost = 0
    shelf = []
    desks = [[] for _ in range(m)]
    
    for student_request in requests:
        for book_id in student_request:
            if book_id in shelf:
                total_cost += shelf.index(book_id) + 1
                shelf.remove(book_id)
            else:
                for i, desk in enumerate(desks):
                    if book_id in desk:
                        total_cost += i + 1
                        desk.remove(book_id)
                        break
                else:
                    total_cost += m + 1
            if len(desks[0]) < c:
                desks[0].append(book_id)
            else:
                for i in range(1, m):
                    if len(desks[i]) < c:
                        desks[i].append(book_id)
                        least_recently_used = min(desks[0], key=lambda x: desks[0][::-1].index(x))
                        desks[0].remove(least_recently_used)
                        shelf.append(least_recently_used)
                        break
                else:
                    shelf.append(book_id)
    
    return total_cost

# Sample Input
print(book_replacement(2, 1, 1, [[50]])) # Output: 4
print(book_replacement(2, 1, 2, [[50], [60]])) # Output: 16
print(book_replacement(3, 1, 2, [[60, 61, 62], [70, 60]])) # Output: 28
print(book_replacement(4, 2, 3, [[60, 61, 62], [70], [80, 81]])) # Output: 68
print(book_replacement(3, 1, 2, [[60, 61, 62], [70, 60]])) # Output: 58
print(book_replacement(1, 2, 5, [[87, 95], [96, 71, 35], [68, 2], [3], [18, 93, 57, 2]])) # Output: 98