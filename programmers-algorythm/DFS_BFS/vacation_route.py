# 여행경로

def solution(tickets):

    answer = []
    tmp = []
    tickets.sort(key=lambda x : (x[0],x[1]))
    ch = [0]*len(tickets)

    def dfs(st) :
        if len(tmp)==len(tickets)+1 :
            answer.append(tuple(tmp))
            return
        else :

            for i, x in enumerate(tickets) :
                if x[0]==st and ch[i]==0 :
                    ch[i] = 1
                    tmp.append(x[1])
                    dfs(x[1])
                    ch[i] = 0
                    tmp.pop()

    for i, x in enumerate(tickets) :
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