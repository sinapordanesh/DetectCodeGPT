def insertionSort(arr,step):
    count = 0
    for i in range(step, len(arr)):
        j = i
        while j >= step and arr[j] < arr[j-step]:
            count += 1
            t = arr[j]
            arr[j] = arr[j-step]
            arr[j-step] = t
            j -= step
    return count
 
def shellSort(arr):
    gaps = [776591, 345152, 153401, 68178, 30301, 13467, 5985, 2660, 1182, 525, 233, 103, 46, 20, 9, 4, 1]
    m = 0
    count = 0
    for step in gaps:
        if step > len(arr):
            continue
        m += 1
        count += insertionSort(arr, step)
    print(m)
    print(" ".join(map(str, gaps[len(gaps)-m:])))
    print(count)
    for num in arr:
        print(num)
 
arr = list()
for _ in range(int(input())):
    arr.append(int(input()))
shellSort(arr)
