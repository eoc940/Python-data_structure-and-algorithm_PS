'''
class Solution:
    def solution(self, s):
        if s == s[::-1] :
            return len(s)
        else : # 펠린드롬 안될때
            mid = len(s)//2
            idx = 0
            while True :
                s += "?"
                idx += 1
                rev = s[::-1]
                if s[idx:len(s)-idx]==rev[idx:len(s)-idx] :
                    return len(s)

c = Solution()
s= "aab"
# abab
# aaba
# bbcd???
# ???dcbb

print(c.solution(s))

# 4번
class Solution:
    def solution(self, price, cost):
        price_cost = []
        for i in range(len(price)):
            price_cost.append((price[i], cost[i]))
        price_cost.sort(key=lambda x: x[0])
        price_list = sorted(list(set(price)))

        answer = dict()
        print(price_list)
        print(price_cost)
        for x in price_list:
            tmp = 0
            for i in price_cost:
                if i[0] >= x:
                    if i[1] >= x:  # 팔 수 있는데 배송비가 그 이상인 경우
                        continue
                    else:
                        print(i, "??")
                        tmp += x - i[1]
            print(tmp)
            answer[x] = tmp
            print(answer)
        if max(answer.values())==0:
            return 0
        else:
            maxi = max(answer.values())
            possible = []
            for j in answer.keys():
                if answer[j] == maxi:
                    possible.append(j)

        return min(possible)

c= Solution()
price = [13,22,35]
cost = [15,30,40]
print(c.solution(price, cost))

#3번
class Solution:
    def solution(self, X, Y, walkTime, sneakTime):
        answer = 0
        if walkTime * 2 < sneakTime:  # 그냥 가로세로로 가는 것이 가장 빠를때
            answer = X * walkTime + Y * walkTime
        elif sneakTime <= walkTime * 2 and walkTime < sneakTime:  # 대각으로 갈땐 sneakTime, 직선으로 갈땐 walkTime
            sneak_cnt = min(X, Y)
            answer = sneak_cnt * sneakTime + walkTime * (X - sneak_cnt) + walkTime * (Y - sneak_cnt)
        elif sneakTime <= walkTime:
            sneak_cnt = min(X, Y)
            answer = sneak_cnt * sneakTime
            # + sneakTime*(X-sneak_cnt) + sneakTime*(Y-sneak_cnt)
            if (X - sneak_cnt) % 2 == 0 and (Y - sneak_cnt) % 2 == 0:
                answer += sneakTime * (X - sneak_cnt) + sneakTime * (Y - sneak_cnt)
            elif (X - sneak_cnt) % 2 == 1 and (Y - sneak_cnt) % 2 == 0:
                answer += sneakTime * (X - sneak_cnt - 1) + walkTime
            elif (X - sneak_cnt) % 2 == 0 and (Y - sneak_cnt) % 2 == 1:
                answer += sneakTime * (Y - sneak_cnt - 1) + walkTime

        return answer

c= Solution()
X = 4
Y = 3
walktime = 5
sneaktime = 4
print(c.solution(X, Y, walktime, sneaktime))
'''


