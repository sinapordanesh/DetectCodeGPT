def reverse_elements(n, elements, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        elements[start:end] = elements[start:end][::-1]
    
    return ' '.join(map(str, elements))

n = int(input())
elements = list(map(int, input().split()))
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

print(reverse_elements(n, elements, queries))