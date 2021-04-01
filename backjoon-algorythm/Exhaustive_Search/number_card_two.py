# 숫자 카드 2

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
search = list(map(int, input().split()))

dic = dict()
for i in cards :
    try :
        dic[i] += 1
    except :
        dic[i] = 1
for j in search :
    try :
        print(dic[j], end=" ")
    except :
        print(0, end=" ")




