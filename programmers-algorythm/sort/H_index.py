# H-INDEX

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for cite in citations:
        cnt = 0
        for num in citations:
            if num >= cite: cnt += 1
            else: break
        if cite >= cnt:
            answer = max(answer, cnt)
    return answer

