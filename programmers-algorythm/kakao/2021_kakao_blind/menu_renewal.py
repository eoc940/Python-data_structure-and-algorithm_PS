# 메뉴 리뉴얼

#combination 조합 사용, counter는 사용 해보지 말아보고 안되면 사용하자
from itertools import combinations

def solution(orders, course):
    answer = []
    # 개수별로 최대를 뽑아야해서 개수로 반복문을 돌림
    for c in course :
        tmp = []
        count_dict = dict()
        # 알파벳 정렬한 order를 조합 구함
        for order in orders :
            tmp.extend(list(combinations(sorted(order), c)))
        # 키가 없다면 넣어주고 키가 있다면 value에 1더함
        for x in tmp :
            if x not in count_dict.keys() :
                count_dict[x] = 1
            else :
                original_value = count_dict[x]
                count_dict[x] = original_value+1
        # 조합이 있을때 -> 만약 orders 중 제일 긴 길이가 3인데 course가 5이면 max못구함
        if count_dict.values() :
            favorite = max(count_dict.values())
        # 최대값이고 2이상일때 답임
        for key, val in count_dict.items() :
            if val==favorite and val>=2:
                answer.append(key)

    answer.sort()
    # 문자열 변환
    for i in range(len(answer)) :
        answer[i] = "".join(answer[i])

    return answer

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))





