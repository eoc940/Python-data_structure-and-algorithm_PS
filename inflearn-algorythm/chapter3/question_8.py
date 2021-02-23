# 곳감(모래시계)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]

def rotate(li, gam) :
    li = list(li)
    gam = list(gam)
    row = li[0]
    left_right = li[1]
    distance = li[2]
    if left_right == 0 :
        gam[row-1] = gam[row-1][distance:] + gam[row-1][:distance]
    elif left_right == 1:
        gam[row-1] = gam[row-1][-distance:] + gam[row-1][:-distance]
    return gam


for i in range(m) :
    a = rotate(b[i], a)

mid = n//2
total = 0
for i in range(n) :
    dist = abs(mid-i)
    total += sum(a[i][mid-dist:mid+dist+1])

print(total)

# 강사님 풀이

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m) :
    h, t, k = map(int, input().split())
    if t == 0 :
        for _ in range(k) :
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k) :
            a[h-1].insert(0, a[h-1].pop())

res = 0
s = 0
e = n-1
for i in range(n) :
    for j in range(s, e+1) :
        res += a[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)