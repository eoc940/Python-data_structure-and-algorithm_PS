# 창고 정리

n = int(input())
box = list(map(int, input().split()))
trial = int(input())

box.sort(reverse=True)
for _ in range(trial) :
    box[0] = box[0]-1
    box[n-1] = box[n-1]+1
    box.sort(reverse=True)

res = box[0] - box[n-1]
print(res)

# 강사님 풀이

L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort()

print(a[L-1]-a[0])









