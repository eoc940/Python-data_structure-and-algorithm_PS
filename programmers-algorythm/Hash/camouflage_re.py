# 위장

from collections import defaultdict
from itertools import combinations

def multi(nums):

    tmp = 1
    for num in nums:
        tmp *= num
    return tmp

def solution(clothes):
    answer = 0
    cloth_dict = defaultdict(int)
    for cloth, kind in clothes:
        cloth_dict[kind] += 1

    for num in range(1, len(cloth_dict)+1):
        combin = combinations(cloth_dict.values(), num)
        for nums in combin:
            answer += multi(nums)

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["dreen_turban", "gear"]]
print(solution(clothes))