# 사과나무(다이아몬드)

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

mid = n//2 # 그냥 나눴을 땐 int붙여줘야함
total = 0

for i in range(n):
    distance = abs(mid-i)
    total += sum(a[i][distance:n-distance])

print(total)

# 강사님 풀이
'''
n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0
s=e=n//2

for i in range(n) :
    for j in range(s, e+1) :
        res += a[i][j]
    if i<n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
'''