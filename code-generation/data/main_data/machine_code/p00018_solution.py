def sort_five_numbers():
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    for num in numbers:
        print(num, end=" ")

sort_five_numbers()