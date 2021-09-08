# 메뉴 리뉴얼
from collections import defaultdict
from itertools import combinations

def make_course(order, course):
    order_list = []
    for i in course:
        for menu in combinations(order, i):
            order_list.append(menu)
    return order_list

def solution(orders, course):
    answer = []
    count_dict = defaultdict(int)
    for order in orders:
        order_list = make_course(sorted(order), course)
        for x in order_list:
            count_dict[x] += 1
    print(count_dict)
    max_dict = defaultdict(int)
    for key, val in count_dict.items():
        if max_dict[len(key)] < val and val >= 2:
            max_dict[len(key)] = val
    print(max_dict)
    for key, val in count_dict.items():
        if max_dict[len(key)] == val:
            answer.append(''.join(key))
    answer.sort()
    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders, course))