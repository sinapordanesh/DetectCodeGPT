def sort_items(items):
    return sorted(items, key=lambda x: (x[0], x[1], x[2], x[3], x[4])) 

# Driver code
n = int(input())
items = []
for _ in range(n):
    items.append(tuple(input().split()))

result = sort_items(items)
for item in result:
    print(" ".join(item))