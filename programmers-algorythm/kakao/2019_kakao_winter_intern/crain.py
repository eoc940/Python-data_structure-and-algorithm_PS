# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    horizontal = []
    result = []
    for i in range(len(board)) :
        tmp = []
        for j in range(len(board)-1,-1,-1) :
            if board[j][i] != 0 :
                tmp.append(board[j][i])
        horizontal.append(tmp)
    for x in moves :
        if horizontal[x-1] :
            result.append(horizontal[x-1].pop())
            if len(result)>=2 and result[-1]==result[-2] :
                answer += 2
                result.pop()
                result.pop()

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))