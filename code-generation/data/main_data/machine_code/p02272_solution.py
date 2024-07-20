def merge_sort(arr):
    comparisons = [0]

    def merge(arr, left, mid, right):
        n1 = mid - left
        n2 = right - mid
        L = arr[left:left+n1]
        R = arr[mid:mid+n2]
        L.append(float('inf'))
        R.append(float('inf'))
        i = j = 0
        for k in range(left, right):
            comparisons[0] += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

    def merge_sort_helper(arr, left, right):
        if left+1 < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid, right)
            merge(arr, left, mid, right)

    merge_sort_helper(arr, 0, len(arr))
    return arr, comparisons[0]