# 쿼드 압축 후 개수 세기

def validate(x, y, leng, arr): # 4,0 이라고 가정
    li = []
    if arr[x][y] == -1: return -1
    stan = arr[x][y]
    for i in range(x, x+leng):
        for j in range(y, y+leng):
            if arr[i][j] != stan:
                return -1
    for i in range(x, x + leng):
        for j in range(y, y + leng):
            arr[i][j] = -1
    return stan

def solution(arr):
    zero, one = 0, 0
    leng = len(arr)
    divide = []
    while leng > 0:
        divide.append(leng)
        leng = leng//2

    for div in divide: # div == 4
        for i in range(len(arr)//div):
            for j in range(len(arr) // div):
                result = validate(div*i, div*j,div, arr)
                if result == 0: zero += 1
                elif result == 1: one += 1

    return [zero, one]

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))

