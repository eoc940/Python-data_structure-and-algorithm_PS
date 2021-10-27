
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    less_arr, equal_arr, more_arr = [], [], []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            more_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(less_arr) + equal_arr + quick_sort(more_arr)

arr = [7,3,3,14,2,63464,2,21,236,685,643,4232]
arr2 = ["df","da","gdgss","gsdgz","cvzx"]
print(quick_sort(arr2))