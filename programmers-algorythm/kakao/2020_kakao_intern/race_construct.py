# 경주로 건설

from collections import deque

def solution(board):
    answer = float('inf')
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dq = deque()
    ch = [[float('inf')]*len(board) for _ in range(len(board))]
    if board[0][1]==0:
        dq.append((0,1,100,1))
    if board[1][0]==0:
        dq.append((1,0,100,0))
    while dq:
        tmp = dq.popleft()
        # print(tmp)
        ch[tmp[0]][tmp[1]] = tmp[2]
        if tmp[0]==len(board)-1 and tmp[1]==len(board)-1:
            answer = min(answer, tmp[2])
            continue
            # print()
            # print()
            # print(answer)
            # print()
            # print()
        else :
            if tmp[2] >= answer :
                continue
        for i in range(4):
            xx = tmp[0] + dx[i]
            yy = tmp[1] + dy[i]
            if 0<=xx<len(board) and 0<=yy<len(board) and board[xx][yy]==0:
                if tmp[3]==1:
                    if tmp[0]==xx:
                        if tmp[2]+100 < ch[xx][yy] and tmp[2]+100 < answer:

                            dq.append((xx,yy,tmp[2]+100,1))
                    else:
                        if tmp[2]+600 < ch[xx][yy] and tmp[2]+600 < answer:

                            dq.append((xx,yy,tmp[2]+600,0))
                else:
                    if tmp[1]==yy:
                        if tmp[2]+100 < ch[xx][yy] and tmp[2]+100 < answer:

                            dq.append((xx,yy,tmp[2]+100,0))
                    else:
                        if tmp[2]+600 < ch[xx][yy] and tmp[2]+600 < answer:

                            dq.append((xx,yy,tmp[2]+600,1))

    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
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