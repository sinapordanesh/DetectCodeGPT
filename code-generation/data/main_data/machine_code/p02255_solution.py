def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(" ".join(str(x) for x in arr))

# Driver code
N = int(input())
sequence = list(map(int, input().split()))

insertion_sort(sequence)