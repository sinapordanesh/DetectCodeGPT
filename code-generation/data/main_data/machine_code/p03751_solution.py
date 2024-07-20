def count_possibilities(n, handles):
    possibilities = 1
    for handle in handles:
        if '?' in handle:
            possibilities *= 26
    return possibilities

n = 2
handles = ['?o?r?s?', '?et?']
print(count_possibilities(n, handles))