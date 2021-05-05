# 정수 삼각형

def solution(triangle):
    dy = []
    for i in range(1,len(triangle)+1) :
        tmp = [0]*i
        dy.append(tmp)
    dy[0][0] = triangle[0][0]

    for i in range(1, len(triangle)) :
        for j in range(i+1) :
            if j==0 :
                dy[i][j] = dy[i-1][j] + triangle[i][j]
            elif j==i:
                dy[i][j] = dy[i-1][j-1] + triangle[i][j]
            else :
                dy[i][j] = max(dy[i-1][j-1], dy[i-1][j]) + triangle[i][j]


    return max(dy[len(triangle)-1])



li = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(li))