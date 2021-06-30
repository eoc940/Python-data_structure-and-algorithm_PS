# 튜플

def solution(s):
    answer = []
    # s가 문자열이므로 중괄호와 , 삭제시킴
    nums = s.lstrip("{").rstrip("}").split("},{")
    # 각 nums의 요소들을 ,기준으로 나누고 다시 넣어줌
    for i in range(len(nums)):
        li = nums[i].split(",")
        nums[i] = li
    # 리스트를 내부 리스트 길이 기준으로 정렬
    nums.sort(key=len)

    # 첫번째 인덱스의 값부터 반복문으로 돌려서 초기에 빈 answer에다가
    # answer에 값이 없을 시 append한다
    for x in nums:
        for j in range(len(x)) :
            if x[j] not in answer :
                answer.append(x[j])

    # 각각의 문자의 리스트로 이루어진 answer를 정수로 바꿔줌
    answer = list(map(int, answer))

    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))