# 퀵 정렬

'''
pivot = arr[rt]
라고 하여 맨 오른쪽의 값보다 작으면 왼쪽으로 붙이고
맨 오른쪽 값보다 크면 오른쪽으로 붙인다.
전위 순회를 이용 : 낮은 레벨의 작업이 끝나고 나서 나누어져서 작업된다
'''

def Qsort(lt, rt) :
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt) :
            if arr[i] <= pivot :
                arr[i], arr[pos] = arr[pos], arr[i] #swap
                pos += 1
        arr[rt], arr[pos] = arr[pos], arr[rt]
        Qsort(lt, pos-1)
        Qsort(pos, rt)



arr = [45,21,23,36,15,67,11,60,20,33]
print("Before sort : ", end=" ")
print(arr)
Qsort(0,9)
print()
print("After sort : ", end=" ")
print(arr)