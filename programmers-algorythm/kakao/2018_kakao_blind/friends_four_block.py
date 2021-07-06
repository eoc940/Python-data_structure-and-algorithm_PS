# 프렌즈 4블록

def erase(x,y,board): # 리스트 리턴해야 함
    block = board[x][y]
    if block == 0:
        return []
    for i in range(x,x+2):
        for j in range(y,y+2):
            if board[i][j]!=block:
                return []
    return [[x,y],[x+1,y],[x,y+1],[x+1,y+1]]

def solution(m, n, board):
    answer = 0
    for i,v in enumerate(board):
        board[i] = list(v)
    # print(board)
    while True :
        erase_list = list()
        for i in range(m-1):
            for j in range(n-1):
                erase_list.extend(erase(i,j,board))

        # print(erase_list)
        # 탐색했는데 지울게 없다면 while문 종료한다
        # print(erase_list, "!!")
        if not erase_list:
            break
        # 지울 리스트를 반복문 돌면서 지워준다
        for x, y in erase_list:
            board[x][y] = 0
        # for x in board:
        #     print(x)
        # print()
        for i in range(n):
            for j in range(m-1,-1,-1):
                if board[j][i]==0:
                    for k in range(j-1,-1,-1):
                        if board[k][i] != 0:
                            board[j][i], board[k][i] = board[k][i], board[j][i]
                            break
        # for x in board:
        #     print(x)
        # print()

    for x in board:
        answer += x.count(0)

    return answer

m=6
n=6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m,n,board))



