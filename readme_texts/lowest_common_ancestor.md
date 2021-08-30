#### 최소 공통 조상(Lowest Common Ancestor) : 기초 문제
- BOJ 'LCA'문제 : https://www.acmicpc.net/problem/11437
- N(2 <= N <= 50000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 
루트는 1번이다. 두 노드의 쌍 M(1 <= M <= 10000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다

#### 최소 공통 조상(Lowest Common Ancestor) 
- 최소 공통 조상(LCA) 문제는 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제이다
- LCA(8번 노드, 15번 노드) -> 2번 노드
![image](https://user-images.githubusercontent.com/67304980/131327206-667dc87c-0689-4b71-8e0a-d7a722c5b3b9.png)

#### 기본적인 최소 공통 조상(LCA) 알고리즘
- 최소 공통 조상 찾기 알고리즘은 다음과 같다
  1. 모든 노드에 대한 깊이(depth)를 계산한다
  2. 최소 공통 조상을 찾을 두 노드를 확인한다
      1. 먼저 두 노드의 깊이(depth)가 동일하도록 거슬러 올라간다
      2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다
  3. 모든 LCA(a,b) 연산에 대하여 2번의 과정을 반복한다

- DFS를 이용해 모든 노드에 대하여 깊이(depth)를 계산할 수 있다
![image](https://user-images.githubusercontent.com/67304980/131327582-1fa39646-f7c2-4154-9f01-31d9705a18d9.png)
- 먼저 두 노드의 깊이를 맞춘 후 거슬러 올라간다

```
import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기
n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프(graph) 정보

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x
        dfs(y, depth + 1)

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이가 동일하도록
    while d[a] != d[b]:
        if d[b] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))
```

#### 기본적인 최소 공통 조상(LCA) 알고리즘 : 시간 복잡도 분석
- 매 쿼리마다 부모 방향으로 거슬러 올라가기 위해 최악의 경우 O(N)의 시간 복잡도가 요구된다
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 O(NM)이다

#### 최소 공통 조상(Lowest Common Ancestor) : 심화 문제
- BOJ 'LCA 2'문제 : https://www.acmicpc.net/problem/11438
- N(2 <= N <= 100000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며,
루트는 1번이다. 두 노드의 쌍 M(1 <= M <= 100000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다

#### 최소 공통 조상(LCA) 알고리즘 개선하기
- 각 노드가 거슬러 올라가는 속도를 빠르게 만드는 방법에 대해 고민해 보자
  - 만약 총 15칸 거슬러 올라가야 한다면?
    - 8칸 -> 4칸 -> 2칸 -> 1칸
- 2의 제곱 형태로 거슬러 올라가도록 하면 O(logN)의 시간 복잡도를 보장할 수 있다
- 메모리를 조금 더 사용하여 각 노드에 대해 2<sup>i</sup>번째 부모에 대한 정보를 기록하자

- 모든 노드에 대하여 깊이(depth)와 2<sup>i</sup>번째 부모에 대한 정보를 계산한다
![image](https://user-images.githubusercontent.com/67304980/131329218-6b607d99-2233-4cc2-bd7d-c7733a210a0f.png)
                              
- LCA(13번 노드, 15번 노드)
  - 먼저 두 노드의 깊이를 맞춘다
![image](https://user-images.githubusercontent.com/67304980/131329386-05561ae3-bf17-4d65-b725-2916d99fafa7.png)
  - 이후에 depth 1(2번 노드, 3번 노드)로 거슬러 올라간다
  - 이후 depth 0(1번 노드)로 거슬러 올라간다

#### 개선된 최소 공통 조상(LCA) 알고리즘 : 시간 복잡도 분석
- 다이나믹 프로그래밍을 이용해 시간 복잡도를 개선할 수 있다
  - 세그먼트 트리를 이용하는 방법도 존재한다
- 매 쿼리마다 부모를 거슬러 올라가기 위하 O(logN)의 복잡도가 필요하다
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 O(MlogN)이다

```
import sys
input = sys.stdin.readline # 시간 초과를 피하기 위한 빠른 입력 함수
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21 # 2^21 = 1000000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프(graph) 정보

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]:
        if c[y]: # 이미 깊이를 구했다면 넘기기
            continue
        parent[y][0] = x
        dfs(y, depth + 1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1,0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][1] = parent[parent[j][i-1]][i-1]
            
# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a
    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:    
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))
```














