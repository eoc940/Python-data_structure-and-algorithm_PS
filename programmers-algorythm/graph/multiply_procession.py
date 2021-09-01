# 행렬의 곱셈

def calculate(li1, li2):
    total = 0
    for i in range(len(li1)):
        total += li1[i] * li2[i]
    return total

def solution(arr1, arr2):
    row, col = len(arr1), len(arr2[0])
    answer = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            li1 = arr1[i]
            li2 = [arr2[k][j] for k in range(len(arr2))]
            #print(li1, li2)
            answer[i][j] = calculate(li1, li2)
    return answer

arr1 = [[2, 3, -2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
print(solution(arr1, arr2))