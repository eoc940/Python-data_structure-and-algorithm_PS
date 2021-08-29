### 트리(Tree)

- 트리는 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조이다
![image](https://user-images.githubusercontent.com/67304980/131254192-2b3d4f72-6046-4262-9636-9351a144b8ff.png)

#### 이진 탐색 트리(Binary Search Tree)
- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종이다
- 이진 탐색 트리의 특징 : 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
  - 부모 노드보다 왼쪽 자식 노드가 작다
  - 부모 노드보다 오른쪽 자식 노드가 크다

![image](https://user-images.githubusercontent.com/67304980/131254326-a1af1912-d1ed-435d-b0bc-1a946508438b.png)

- 이진 탐색 트리가 이미 구성되어 있다고 가정하고 데이터를 조회하는 과정을 살펴보자
- 찾고자 하는 원소 : 37
- [Step 1] 루트 노드부터 방문하여 탐색을 진행한다
![image](https://user-images.githubusercontent.com/67304980/131254402-1f0d87f4-46f4-4ab3-9bf9-1da2c3a63ac6.png)
- [Step 2] 현재 노드와 값을 비교한다
![image](https://user-images.githubusercontent.com/67304980/131254461-097fbe83-95da-4b7d-9804-f360f8709452.png)
- [Step 3] 현재 노드와 값을 비교한다
![image](https://user-images.githubusercontent.com/67304980/131254510-50d3c9ee-ba86-4530-b05a-3942c299b629.png)

#### 트리의 순회(Tree Traversal)
- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미한다
  - 트리의 정보를 시각적으로 확인할 수 있다
- 대표적인 트리 순회 방법은 다음과 같다
  - 전위 순회 : 루트를 먼저 방문한다
  - 중위 순회 : 왼쪽 자식을 방문한 뒤에 루트를 방문한다
  - 후위 순회 : 오른쪽 자식을 방문한 뒤에 루트를 방문한다

![image](https://user-images.githubusercontent.com/67304980/131254605-7af0138b-64d2-4ec9-89fc-b629b0d05352.png)

```
class Node:
    def __init__(self, data, left_node, right_node):   
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회
def pre_order(node):
    print(node, data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node, data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
        
# 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node, data, end=' ')
    
n = int(input())
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
```









