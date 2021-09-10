# 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for candi in skill_trees:
        ch = list()
        for sk in skill:
            loca = candi.find(sk)
            if loca == -1 : loca = 100
            ch.append(loca)
        sorted_ch = sorted(ch)

        if ch == sorted_ch: answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))