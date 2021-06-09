# 여행경로

def solution(tickets):
    global answer
    answer = []
    tmp = []
    # airport = set()
    # for x in tickets :
    #     airport.update(x)
    tickets.sort(key=lambda x : (x[0],x[1]))
    ch = [0]*len(tickets)

    def dfs(v, st) :
        global answer
        # print(v)
        # print(tmp)
        if len(tmp)==len(tickets)+1 :
            answer.append(tuple(tmp))
            return
        else :

            for i, x in enumerate(tickets) :
                if x[0]==st and ch[i]==0 :
                    ch[i] = 1
                    #print(v+1)
                    tmp.append(x[1])
                    dfs(v+1, x[1])
                    ch[i] = 0
                    tmp.pop()

    for i, x in enumerate(tickets) :
        if x[0]=="ICN" :
            ch[i] = 1
            tmp.append(x[0])
            tmp.append(x[1])
            dfs(0, x[1])
            ch[i] = 0
            tmp.pop()
            tmp.pop()
    #print(tickets)
    return list(answer[0])


#tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets = [['ICN','GGG'],['ICN','YYY'],['YYY','ICN']]
print(solution(tickets))