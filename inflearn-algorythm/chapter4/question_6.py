# 씨름 선수(그리디)

# 170 72
# 172 67
# 180 70
# 181 60
# 183 65
'''
n = int(input())
info = []
for i in range(n):
    h, w = map(int,input().split())
    info.append((h,w))
info.sort(key=lambda x:x[0])

cnt = 0
for i in range(n) :
    max_weight = info[i][1]
    for j in range(i,n) :
        if info[j][1] > max_weight :
            max_weight = info[j][1]
    if max_weight == info[i][1] :
        cnt += 1
print(cnt)
'''
# 강사님 풀이
# 키 역순으로 정렬한뒤 몸무게 최대값인지 아닌지를 판별
n = int(input())
info = []
for i in range(n):
    h, w = map(int,input().split())
    info.append((h,w))
info.sort(reverse=True,key=lambda x:x[0])
cnt = 0
largest = 0
for h,w in info :
    if w > largest :
        largest = w
        cnt += 1
print(cnt)



