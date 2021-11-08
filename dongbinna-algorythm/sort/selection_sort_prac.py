# 선택정렬

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                min_value = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [5,2,63,3,53,12,3,53,63,534,1,4,23]
print(selection_sort(arr))