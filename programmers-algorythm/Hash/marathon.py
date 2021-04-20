# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            return participant[i]
    return participant.pop()

par = ["marina", "josipa", "nikola", "vinko", "filipa"]
com = ["josipa", "filipa", "marina", "nikola"]

print(solution(par, com))
