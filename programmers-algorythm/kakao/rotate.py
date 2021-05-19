# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    board = []
    board.append([0]*(columns+1))
    number = 0
    for i in range(rows) :
        tmp = [0]
        for j in range(columns) :
            number += 1
            tmp.append(number)
        board.append(tmp)
    # for x in board :
    #     print(x)
    for query in queries :
        rotate_num = []
        st_row, st_col, en_row, en_col = query[0],query[1],query[2],query[3]
        #print(st_row, st_col, en_row, en_col)
        for i in range(st_col, en_col+1) :
            rotate_num.append(board[st_row][i])
        for i in range(st_row+1, en_row+1) :
            rotate_num.append(board[i][en_col])
        for i in range(en_col-1, st_col-1,-1) :
            rotate_num.append(board[en_row][i])
        for i in range(en_row-1, st_row,-1) :
            rotate_num.append(board[i][st_col])
        #print(rotate_num)
        answer.append(min(rotate_num))
        last_num = rotate_num.pop()
        rotate_num.insert(0, last_num)
        idx = 0
        for i in range(st_col, en_col+1) :
            board[st_row][i] = rotate_num[idx]
            idx += 1
        for i in range(st_row+1, en_row+1) :
            board[i][en_col] = rotate_num[idx]
            idx += 1
        for i in range(en_col-1, st_col-1,-1) :
            board[en_row][i] = rotate_num[idx]
            idx += 1
        for i in range(en_row-1, st_row,-1) :
            board[i][st_col] = rotate_num[idx]
            idx += 1
        #for x in board:
            #print(x)

    return answer

rows = 100
columns = 97
queries = [[1,1,100,97]]

print(solution(rows, columns, queries))

