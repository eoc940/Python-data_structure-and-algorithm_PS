import heapq

# 1번예
nums2 = [7,4,8,3,2,6]

heapq.heapify(nums2)
print(nums2)
print()

# 2번예
nums = [4, 1, 7, 3, 8, 5]
heap1 = []

for num in nums:
    heapq.heappush(heap1, num)  # (힙, 값)

print(heap1)
print()

# 3번예
nums = [6, 2, 7, 9, 8, 5]
heap2 = []

for num in nums:
    heapq.heappush(heap2, (-num,num)) # (힙, (우선 순위, 값))

while heap2:
    # 튜플로 저장되있고 1번 인덱스가 값임
    print(heapq.heappop(heap2)[1], end=" ")




