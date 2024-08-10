def count_triples(N):
    for i in range(1, N+1):
        count = 0
        for x in range(1, i+1):
            for y in range(1, i+1):
                for z in range(1, i+1):
                    if x**2 + y**2 + z**2 + x*y + y*z + z*x == i:
                        count += 1
        print(count)

# Input
N = int(input())

# Call the function
count_triples(N)