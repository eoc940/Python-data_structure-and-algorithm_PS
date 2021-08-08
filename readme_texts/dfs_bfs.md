### 그래프 탐색 알고리즘 : DFS/BFS
- 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다
- 대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있다
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야 한다

##### 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다
- 파이썬에서는 리스트 자료구조를 사용하면 된다
- append, pop함수의 시간복잡도는 O(1)이다

##### 큐 자료구조
- 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조이다
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화할 수 있다
- 파이썬에서는 deque 자료구조를 사용하는 것이 좋다
- append, popleft함수의 시간복잡도는 O(1)이다

##### 재귀 함수
- 재귀 함수란 자기 자신을 다시 호출하는 함수이다
- 스택 자료구조에 함수에 대한 정보가 차례로 메모리에 담기는 형태이다
- 따라서 무한정으로 재귀 함수가 호출되면 에러가 발생한다
- 재귀 함수를 문제 풀이에서 사용할 때는 종료 조건을 명시해야 한다
- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다
- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 내부의 스택 프레임에 쌓인다 -> 스택 대신 재귀를 이용하는 경우가 많다

##### DFS
- DFS는 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다
- 스택 자료구조 혹은 재귀 함수를 이용하며 동작 과정은 다음과 같다
    - 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다
    - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
    - 더 이상 위의 과정을 수행할 수 없을 때까지 반복한다
    
##### BFS
- BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다
- BFS는 큐 자료구조를 이용하며 동작 과정은 다음과 같다
    - 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
    - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다
    - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다
```
# 음료수 얼려 먹기

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
ices = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    global answer
    dq = deque()
    dq.append((x,y))
    ices[x][y] = 1
    while dq:
        tx, ty = dq.popleft()
        for i in range(4):
            xx = tx + dx[i]
            yy = ty + dy[i]
            if 0<=xx<n and 0<=yy<m and ices[xx][yy] == 0:
                ices[xx][yy] = 1
                dq.append((xx,yy))
    answer += 1

for i in range(n):
    for j in range(m):
        if ices[i][j] == 0: bfs(i,j)

print(answer)
```
```
# 미로 탈출

import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
answer = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

dq = deque()
dq.append((0,0))


while dq:
    for _ in range(len(dq)):
        tx, ty = dq.popleft()
        if tx == n-1 and ty == m-1 :
            answer = maze[tx][ty]
            break
        for i in range(4):
            x = tx + dx[i]
            y = ty + dy[i]
            if 0<=x<n and 0<=y<m and maze[x][y]==1:
                maze[x][y] = maze[tx][ty] + 1
                dq.append((x,y))
    for x in maze:
        print(x)
    print()

print(answer)
```
