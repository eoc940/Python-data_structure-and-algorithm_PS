# 14889 스타트와 링크



from itertools import permutations, combinations
import sys

n = int(sys.stdin.readline().rstrip())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
members = [x for x in range(n)]
team1_candidate = combinations(members, len(members)//2)

answer = float('inf')
for team1 in team1_candidate:
    # 전체 리스트를 반복문으로 돌면서 group1에 속하지 않는 것만 선택
    team2 = tuple(x for x in members if x not in team1)
    # print(team1, team2)
    team1_permut = permutations(team1, 2)
    team2_permut = permutations(team2, 2)
    # print(tuple(team1_ability), tuple(team2_ability))
    team1_ability, team2_ability = 0,0
    for x,y in team1_permut:
        team1_ability += ability[x][y]
    for x,y in team2_permut:
        team2_ability += ability[x][y]
    answer = min(answer, abs(team1_ability - team2_ability))

print(answer)
