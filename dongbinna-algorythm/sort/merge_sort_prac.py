# 병합 정렬

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    # divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # conquer
    result = list()
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # append rest
    result += left[l:]
    result += right[r:]
    return result



arr = [5,2,63,3,53,12,3,53,63,534,1,4,23]
print(merge_sort(arr))