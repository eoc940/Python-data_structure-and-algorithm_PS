# 가장 큰 정사각형 찾기


def solution(board):
    if len(board) == 1: return max(board[0])
    elif len(board[0]) == 1: return int(str(max(board))[1])

    length = 0
    # 가로, 세로가 최소 2
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min([board[i-1][j], board[i][j-1], board[i-1][j-1]])+1
                length = max(length, board[i][j])
    return length**2

board = [[0],[0]]
print(solution(board))



# def calculate(board, i, j, max_len):
#     for x in range(i, i+max_len):
#         for y in range(j, j+max_len):
#             if board[x][y] == 0:
#                 return False
#     return True
#
# def solution(board):
#     answer = 0
#     row, col = len(board), len(board[0])
#     max_len = min(row, col)
#     while max_len > 0:
#         for i in range(row - max_len + 1):
#             for j in range(col - max_len + 1):
#                 if board[i][j] == 1:
#                     if calculate(board, i, j, max_len):
#                         return max_len**2
#         max_len -= 1
#     return 0
#
# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# print(solution(board))






