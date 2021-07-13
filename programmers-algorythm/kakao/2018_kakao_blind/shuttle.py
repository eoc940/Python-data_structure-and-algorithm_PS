# 셔틀 버스
def depart_time(n,t):
    depart = []
    for i in range(n):
        depart.append(60*9 + t*i)
    return depart

def convert_timetable(timetable):
    timetables = []
    for x in timetable:
        hour, minute = x.split(":")
        tmp = 0
        tmp += int(hour)*60
        tmp += int(minute)
        timetables.append(tmp)
    return timetables

def solution(n, t, m, timetable):
    answer = ''
    depart = depart_time(n,t)
    timetables = convert_timetable(timetable)
    depart.sort()
    timetables.sort()
    # print(depart)
    # print(timetables)
    ch = [0] * len(timetables)
    is_full = False
    for i,departure in enumerate(depart):
        cnt = 0
        for idx,time in enumerate(timetables):
            if time <= departure and ch[idx] == 0 and cnt < m:
                cnt += 1
                ch[idx] = 1
        if cnt==m and i==len(depart)-1:
            is_full = True
    # print(is_full)
    # print(ch)
    if not is_full:
        answer = depart[-1]
        return '%02d:%02d' %(answer//60, answer%60) # 손봐야함
    if is_full:
        for i in range(len(ch)-1,-1,-1):
            if ch[i]==1:
                answer = timetables[i] - 1
                return '%02d:%02d' %(answer//60, answer%60) # 손봐야함

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(solution(n,t,m,timetable))