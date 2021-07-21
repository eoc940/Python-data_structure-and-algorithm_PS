# 여행경로

def solution(tickets):
    answer = []

    def dfs(L,st,en):
        if L == len(tickets):
            answer.append(tuple(tmp))
            return
        else:
            for i,loca in enumerate(tickets):
                if ch[i] == 0 and en == loca[0]:
                    ch[i] = 1
                    tmp.append(loca[1])
                    dfs(L+1, loca[0], loca[1])
                    tmp.pop()
                    ch[i] = 0

    tickets.sort(key=lambda x : (x[0],x[1]))
    print(tickets)
    ch = [0]*len(tickets)
    tmp = []
    for i,loca in enumerate(tickets):
        if loca[0] == "ICN":
            tmp.append(loca[0])
            tmp.append(loca[1])
            ch[i] = 1
            dfs(1,loca[0],loca[1])
            ch[i] = 0
            tmp.pop()
            tmp.pop()
    print(answer)
    return list(answer[0])


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))





















'''
def solution(tickets):

    answer = []
    tmp = []
    # 알파벳 순으로 방문해야 하므로 tickets를 먼저 정렬함
    tickets.sort(key=lambda x : (x[0],x[1]))
    # 방문 여부 즉 tickets의 각 값들(출발,도착)을 지났는지 체크
    ch = [0]*len(tickets)

    def dfs(st) :
        # tmp 길이가 tickets의 길이보다 1 길면 다 방문 한 것
        # 그때 tmp를 answer에 넣어준다
        if len(tmp)==len(tickets)+1 :
            answer.append(tuple(tmp))
            return
        else :
            # dfs의 배개변수와 tickets의 출발지가 일치하면 ch하고 dfs
            for i, x in enumerate(tickets) :
                if x[0]==st and ch[i]==0 :
                    ch[i] = 1
                    tmp.append(x[1])
                    dfs(x[1])
                    ch[i] = 0
                    tmp.pop()


    for i, x in enumerate(tickets) :
        # 출발이 ICN일때 출발과 도착을 tmp에 넣고 dfs돌린다
        if x[0]=="ICN" :
            ch[i] = 1
            tmp.append(x[0])
            tmp.append(x[1])
            dfs(x[1])
            ch[i] = 0
            tmp.pop()
            tmp.pop()
    return list(answer[0])


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
#tickets = [['ICN','GGG'],['ICN','YYY'],['YYY','ICN']]
print(solution(tickets))
'''