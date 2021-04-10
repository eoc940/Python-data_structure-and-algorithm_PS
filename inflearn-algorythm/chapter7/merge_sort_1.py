# 병합 정렬

'''
병합정렬은 일단 리스트를 절반으로 나눈다
D(0,7)에서 인자값은 처음과 끝의 인덱스이므로 mid=(0+7)//2 -> 3
따라서 D(0,7)은 D(0,3)과 D(4,7)을 호출한다.
두 가지 호출한 것을 다 끝마치고 오면 D(0,7)본연의 일(합치는 일)을 수행한다.
'''

def Dsort(lt, rt) :
    if lt<rt:
        mid = (lt+rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1<=mid and p2<=rt :
            if arr[p1] < arr[p2] :
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        #어느쪽 한쪽이 끝남
        if p1<=mid : tmp=tmp+arr[p1:mid+1]
        if p2<=rt : tmp=tmp+arr[p2:rt+1]
        for i in range(len(tmp)) :
            arr[lt+i]=tmp[i]


arr = [23,11,45,36,15,67,33,21]
print("Before sort : ", end=" ")
print(arr)
Dsort(0,7)
print()
print("After sort : ", end=" ")
print(arr)

