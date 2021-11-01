# 풍선 터뜨리기

def solution(a):
    answer = 0
    left, right = float('inf'), float('inf')
    ch = [0 for _ in range(len(a))]
    for i in range(len(a)):
        if a[i] < left:
            ch[i] = 1
            left = a[i]
        if a[-i-1] < right:
            ch[-i-1] = 1
            right = a[-i-1]


    return sum(ch)

a = [9,-9,-5]
print(solution(a))