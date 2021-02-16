# 소수(에라토스테네스 체)
'''
n = int(input())
cnt = 0


for j in range(2, n+1) :
    flag = True
    for i in range(2,j) :
        if j%i == 0 :
            flag = False
            break
    if flag :
        cnt += 1
print(cnt)
'''

# 강사님 풀이(빠른 방법)

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2,n+1) :
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i) :
            ch[j] = 1
print(cnt)
