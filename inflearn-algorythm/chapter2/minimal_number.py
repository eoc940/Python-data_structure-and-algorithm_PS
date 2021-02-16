# 최솟값 구하기

arr=[5,3,7,9,2,5,2,6]
arr_min = float('inf') # 파이썬에서 가장 큰 값이 저장됨
# 혹은 arr_min = arr[0] 으로 설정해도 상관없음

for i in range(len(arr)) :
    if arr[i] < arr_min :
        arr_min = arr[i]
print(arr_min)



