def devide(x, y) :
    a=[]
    for i in range(1, x+1) :
        if x%i == 0 :
            a.append(i)
    if len(a) >= y :
        return a[y-1]
    else:
        return -1

n, k=map(int, input().split(" "))
print(devide(n,k))
'''
# 강사님 풀이
n, k=map(int, input().split(" "))
cnt=0
for i in range(1, n+1) :
    if n%i==0 :
        cnt += 1
    if cnt==k :
        print(i)
        break
else :
    print(-1)
'''
