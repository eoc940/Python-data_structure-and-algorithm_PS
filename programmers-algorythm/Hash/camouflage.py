# 위장

from collections import defaultdict


def solution(clothes):
    answer = 1
    cloth = defaultdict(int)
    for name, kind in clothes :
        cloth[kind] += 1

    for v in cloth.values():
        answer *= (v+1)

    return answer - 1


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))