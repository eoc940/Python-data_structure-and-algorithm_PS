
from collections import deque

def solution(places):
    answer = []
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for pl in places : #대기실 별로 나눠서 반복 돌림
        print(pl)
        step_answer = 1
        for i in range(5) :
            for j in range(5) :

                dq = deque()
                if pl[i][j] == "P" :
                    ch = [[0]*5 for _ in range(5)]
                    dq.append((i,j))
                    ch[i][j] = 1


                    while dq :
                        tmp = dq.popleft()
                        for k in range(4) :
                            x = tmp[0] + dx[k]
                            y = tmp[1] + dy[k]
                            if 0<=x<=4 and 0<=y<=4 and pl[x][y]!="X" and ch[x][y]==0:
                                #print(x,y)
                                if pl[x][y]=="P" :
                                    #print(pl[x][y])
                                    if abs(x-i)+abs(y-j)<=2:
                                        step_answer=0
                                    dq.clear()
                                else : # pl[x][y]=="O"
                                    dq.append((x,y))
                                    ch[x][y] = 1

        answer.append(step_answer)

    return answer

placeses = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(placeses))

