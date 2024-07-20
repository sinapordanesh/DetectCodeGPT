def calculate_change():
    N = int(input())
    change = 1000 - (N % 1000)
    print(change) 

calculate_change()