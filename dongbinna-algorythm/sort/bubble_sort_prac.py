# 버블 정렬


def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort_two(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [3,5,3,7,45,1,2,77,58,99,10]
print(bubble_sort(arr))
print(bubble_sort_two(arr))