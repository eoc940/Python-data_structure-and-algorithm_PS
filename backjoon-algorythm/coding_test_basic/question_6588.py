# 6588 골드바흐의 추측

# 교훈 : 소수인지 아닌지 찾을때 in 키워드를 쓰면 시간복잡도가 O(n)이지만
# 리스트에서 index로 접근해서 찾을 경우 시간복잡도가 O(1)이다

import sys

#sosu = []
n = 1000000
ch = [False, False] + [True]*(n-1)
for i in range(2,n+1):
    if ch[i]:
        #sosu.append(i)
        for j in range(i*2, n+1, i):
            ch[j] = False


def gold_predict(num):
    first = 3
    second = num - 3
    while first <= second:
        if ch[first] and ch[second]:
            return (first, second)
        first += 2
        second -= 2
    return "Goldbach's conjecture is wrong."

while True:
    num = int(sys.stdin.readline().rstrip())
    if num == 0: break
    answer = gold_predict(num)
    if type(answer)==tuple:
        print("%d = %d + %d" %(num, answer[0], answer[1]))
    elif type(answer)==str:
        print(answer)








