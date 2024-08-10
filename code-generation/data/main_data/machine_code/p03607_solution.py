def numbers_written_on_sheet(N, A):
    numbers = set()
    for num in A:
        if num in numbers:
            numbers.remove(num)
        else:
            numbers.add(num)
    return len(numbers)