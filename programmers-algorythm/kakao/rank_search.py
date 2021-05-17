# 순위 검색

def solution(info, query):
    answer = []
    info_list = []
    query_list = []
    # 리스트에 넣어주기


    for x in info :
        info_list.append(x.split(" "))
    for x in query :
        query_list.append(x.replace("and ", "").split(" "))
    #print(info_list)
    #print(query_list)
    for q in query_list :
        cnt = 0
        for i in info_list :
            if int(q[4]) > int(i[4]) :
                continue
            if q[0]!='-' and q[0] != i[0] :
                continue
            if q[1]!='-' and q[1] != i[1] :
                continue
            if q[2]!='-' and q[2] != i[2] :
                continue
            if q[3]!='-' and q[3] != i[3] :
                continue
            cnt += 1
        answer.append(cnt)



    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))