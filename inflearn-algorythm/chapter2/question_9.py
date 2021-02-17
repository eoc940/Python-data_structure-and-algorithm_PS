# 주사위 게임
'''
def get_prize(a,b,c) :
    li = [a,b,c]
    if len(set(li)) == 1 :
        return 10000+1000*li[0]
    elif len(set(li)) == 2 :
        li.sort(reverse=True)
        return 1000+100*li[0]
    else:
        li.sort(reverse=True)
        return 100*li[0]

n = int(input())
max = 0
for i in range(n) :
    a,b,c = map(int, input().split())
    if get_prize(a,b,c) > max :
        max = get_prize(a,b,c)
        res = max

print(res)
'''

# 강사님 풀이

n = int(input())
res = 0
for i in range(n) :
    tmp = input().split()
    tmp.sort()
    a,b,c=map(int,tmp)
    if a==b and b==c :
        money = 10000+(a*1000)
    elif a==b or a==c : # if 의 경우 포함할수 있지만 if에서 걸리면 그냥 넘어가니까 괜찮음
        money = 1000+(a*100)
    elif b==c :
        money = 1000+(b*100)
    else :
        money = c*100
    if money > res :
        res = money

print(res)
