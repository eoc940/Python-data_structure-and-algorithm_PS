# 풍선 터뜨리기

def solution(a):
    left_val, right_val = float('inf'), float('inf')
    ch = [0 for _ in range(len(a))]
    for i in range(len(a)):
        if a[i] < left_val:
            left_val = a[i]
            ch[i] = 1
        if a[-i-1] < right_val:
            right_val = a[-i-1]
            ch[-i-1] = 1

    return sum(ch)

a = [-16,27,65,-2,58,-92,-71,-68,-61]
print(solution(a))