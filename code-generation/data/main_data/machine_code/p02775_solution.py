def min_banknotes(N):
    count = 0
    banknotes = [10**i for i in range(100)] # All possible banknotes
    banknotes.sort(reverse=True)
    
    for value in banknotes:
        while N - value >= 0:
            N -= value
            count += 1
    
    return count

N = int(input())
print(min_banknotes(N))