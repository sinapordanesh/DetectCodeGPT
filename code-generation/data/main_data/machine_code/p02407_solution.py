def reverse_numbers():
    n = int(input())
    sequence = list(map(int, input().split()))
    reversed_sequence = sequence[::-1]
    for num in reversed_sequence:
        print(num, end=" ")

reverse_numbers()