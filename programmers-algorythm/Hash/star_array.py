# 스타 수열

from collections import defaultdict

def solution(a):
    answer = 0
    num_loca = defaultdict(list)
    for i, num in enumerate(a):
        num_loca[num].append(i)

    num_loca_list = list()
    for key, val in num_loca.items():
        num_loca_list.append([key, val])

    num_loca_list.sort(key=lambda x : len(x[1]), reverse=True)

    for key, val in num_loca_list:
        if len(val) * 2 <= answer:
            break
        ch = [0 for _ in range(len(a))]
        total = 0
        for idx in val:
            # 왼쪽 수를 체크
            if 0 <= idx-1 and ch[idx-1] == 0 and a[idx-1] != key:
                ch[idx] = 1
                ch[idx-1] = 1
                total += 2
            # 오른쪽 수를 체크
            elif idx+1 < len(a) and ch[idx+1] == 0 and a[idx+1] != key:
                ch[idx] = 1
                ch[idx+1] = 1
                total += 2

        answer = max(answer, total)

    return answer

a = [5,2,3,3,5,3]
print(solution(a))




