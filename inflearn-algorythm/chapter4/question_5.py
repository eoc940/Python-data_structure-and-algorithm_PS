# 회의실 배정(그리디)

n = int(input())
time_list = [list(map(int, input().split())) for _ in range(n)]

time_list.sort(key=lambda x:x[1])

cnt = 1
# 2 3
# 1 4
# 3 5
# 4 6
# 5 7
criteria = time_list[0][1]

for i in range(n):
    if i==n-1 :
        break
    if criteria <= time_list[i+1][0] :
        cnt += 1
        criteria = time_list[i+1][1]
print(cnt)

# 강사님 풀이

n = int(input())
meeting = []
for i in range(n):
    s,e = map(int, input().split())
    meeting.append((s,e)) # 튜플 형태로 넣는다
meeting.sort(key=lambda x:(x[1],x[0]))

et = 0
cnt = 0
for s, e in meeting :
    if s>=et :
        et = e
        cnt += 1
print(cnt)
