def train_configurations(arrival):
    n = len(arrival)
    return n*(n+1)//2

m = int(input())
for _ in range(m):
    arrival = input()
    print(train_configurations(arrival))