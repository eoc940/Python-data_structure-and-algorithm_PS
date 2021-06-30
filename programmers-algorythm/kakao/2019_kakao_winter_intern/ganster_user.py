# 불량 사용자

from itertools import permutations

def check(names, bans):
    for i in range(len(names)):
        if len(names[i]) != len(bans[i]):
            return False
        for j in range(len(names[i])):
            if bans[i][j] != "*":
                if names[i][j] != bans[i][j]:
                    return False
    return True

def solution(user_id, banned_id):
    answer = set()
    for x in permutations(user_id, len(banned_id)):
        if check(x, banned_id):
            li = list(x)
            li.sort()
            a= tuple(li)
            answer.add(a)
    return len(answer)

user_id =["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
