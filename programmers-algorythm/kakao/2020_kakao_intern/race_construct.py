# 경주로 건설

import sys
from collections import deque

def solution(board):
    answer = sys.maxsize
    direction = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]} # 0:북 1:동 2:남 3:서
    ch = [[float('inf')]*len(board) for _ in range(len(board))]
    ch[0][0] = 0
    dq = deque()
    dq.append((0,0,0,1)) # x,y,total,direction
    dq.append((0,0,0,2))
    while dq:
        x,y,total,direct = dq.popleft()
        # print(x,y,total,direct)
        if x==len(board)-1 and y==len(board)-1:
            if total < answer :
                answer = total
        else:
            for i in range(4):
                xx = x + direction[i][0]
                yy = y + direction[i][1]
                if 0<=xx<len(board) and 0<=yy<len(board) and board[xx][yy]==0:
                    if i != direct:
                        tot = total + 600
                    else :
                        tot = total + 100
                    if tot <= ch[xx][yy]:
                        ch[xx][yy] = tot
                        dq.append((xx,yy,tot,i))

    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))


























'''
import copy, sys

def solution(board):
    global answer
    answer = float('inf')
    ch = [[0]*len(board) for _ in range(len(board))]

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def dfs(x,y,total,way):
        #print(x,y,total,way)
        global answer
        if total > answer:
            return
        if x==len(board)-1 or y==len(board)-1:
            if 100*(len(board)-1-x + len(board)-1-y) + total > answer:
                return
        else :
            if 500 + 100*(len(board)-1-x + len(board)-1-y) + total > answer:
                return
        if x==len(board)-1 and y==len(board)-1:
            answer = min(answer, total)
            #print(answer)
            return
        else :
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx<len(board) and 0<=yy<len(board) and ch[xx][yy]==0 and board[xx][yy]==0:
                    if way=="hori":
                        if x==xx:
                            ch[xx][yy] = 1
                            dfs(xx,yy,total+100,"hori")
                            ch[xx][yy] = 0
                        else:
                            ch[xx][yy] = 1
                            dfs(xx,yy,total+600,"vert")
                            ch[xx][yy] = 0
                    else:
                        if y==yy:
                            ch[xx][yy] = 1
                            dfs(xx,yy,total+100,"vert")
                            ch[xx][yy] = 0
                        else:
                            ch[xx][yy] = 1
                            dfs(xx,yy,total+600,"hori")
                            ch[xx][yy] = 0

    ch[0][0] = 1
    if board[0][1] == 0:
        ch[0][1] = 1
        dfs(0,1,100,"hori")
        ch[0][1] = 0
    if board[1][0] == 0:
        ch[1][0] = 1
        dfs(1,0,100,"vert")
        ch[1][0] = 0

    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
'''