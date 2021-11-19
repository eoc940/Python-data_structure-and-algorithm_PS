# 모두 0으로 만들기
import sys
from collections import defaultdict
sys.setrecursionlimit(300000)
def dfs(x, a, tree, ch):
    global answer
    ch[x] = 1

    for y in tree[x]:
        if not ch[y]:
            a[x] += dfs(y, a, tree, ch)

    answer += abs(a[x])
    return a[x]


def solution(a, edges):
    global answer
    answer = 0
    if sum(a) != 0: return -1

    tree = defaultdict(list)

    for node1, node2 in edges:
        tree[node1].append(node2)
        tree[node2].append(node1)

    ch = [0 for _ in range(len(a))]

    dfs(1, a, tree, ch)

    return answer

a = [-5,0,2,1,2]
edges = [[0,1],[3,4],[2,3],[0,3]]
print(solution(a, edges))
