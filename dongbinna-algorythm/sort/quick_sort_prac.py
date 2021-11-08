
def quick_sort(arr, start, end):
    if start >= end:
        return
    # pivot
    pivot = (start+end) // 2
    pivot_value = arr[pivot]

    left = start
    right = end
    while left <= right:
        while arr[left] < pivot_value:
            left += 1
        while arr[right] > pivot_value:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left],
            left += 1
            right -= 1
    quick_sort(arr, start, right)
    quick_sort(arr, left, end)
    return arr


arr = [7,3,3,14,2,63464,2,21,236,685,643,4232,1,9,98]

print(quick_sort(arr, 0, len(arr)-1))


