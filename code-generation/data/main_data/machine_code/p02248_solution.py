def string_search():
    T = input().strip()
    P = input().strip()
    indices = []
    
    for i in range(len(T)):
        if T[i:i+len(P)] == P:
            indices.append(i)
    
    for index in indices:
        print(index)

string_search()