# 교점에 별 만들기

from itertools import combinations

def solution(line):
    answer = []
    result = []
    meet = []

    for sp1, sp2 in combinations(line, 2):
        a,b,e = sp1
        c,d,f = sp2
        if a*d == b*c:
            continue
        x = (b*f - e*d) / (a*d - b*c)
        y = (e*c - a*f) / (a*d - b*c)
        if int(x) == x and int(y) == y:
            meet.append([int(x),int(y)])
    # print(meet)
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    for x, y in meet:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    for i in range(len(meet)):
        meet[i][0] -= min_x
        meet[i][1] -= min_y
    leng_x = max_x - min_x
    leng_y = max_y - min_y
    # print(meet)
    answer = [['.' for _ in range(leng_x+1)] for _ in range(leng_y+1)]
    for x, y in meet:
        answer[abs(leng_y - y)][x] = "*"

    for arr in answer:
        result.append(''.join(arr))

    return result

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
