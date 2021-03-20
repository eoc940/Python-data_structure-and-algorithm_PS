# 인접행렬

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(m)]
res = [[0]*n for _ in range(n)]

for i in range(m) :
    res[a[i][0]-1][a[i][1]-1] = a[i][-1]

for j in range(n) :
    for k in range(n) :
        print(res[j][k], end=" ")
    print()



