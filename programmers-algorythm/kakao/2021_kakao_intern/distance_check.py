# 거리 확인하기

from collections import deque

def check_dist(place) :
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                ch = [[0]*5 for _ in range(5)]
                dq = deque()
                ch[i][j] = 1
                dq.append((i,j))
                while dq:
                    for _ in range(len(dq)):
                        tmp = dq.popleft()
                        if place[tmp[0]][tmp[1]]=="P" and tmp != (i,j):
                            #print(ch)
                            if ch[tmp[0]][tmp[1]] <= 3:

                                return 0
                            else :
                                dq.clear()
                                break
                        for k in range(4):
                            x = tmp[0] + dx[k]
                            y = tmp[1] + dy[k]
                            if 0<=x<5 and 0<=y<5 and ch[x][y]==0 and place[x][y] != 'X' :
                                ch[x][y] = ch[tmp[0]][tmp[1]] + 1
                                dq.append((x,y))

    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check_dist(place))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))