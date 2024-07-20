def expected_number_of_operations(N, dishes):
    total_sushi = sum(dishes)
    expected_operations = 0
    
    while total_sushi > 0:
        for i in range(N):
            if dishes[i] > 0:
                expected_operations += 1 / (dishes[i] / total_sushi)
                dishes[i] -= 1
                total_sushi -= 1
                
    return expected_operations

N = int(input())
dishes = list(map(int, input().split()))

print(expected_number_of_operations(N, dishes))