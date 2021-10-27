class MaxHeap:
    def __init__(self):
        self.queue = []

    def parent(self, idx):
        return (idx-1) // 2

    def left_child(self, idx):
        return idx*2+1

    def right_child(self, idx):
        return idx*2 + 2

    def swap(self, parent, last):
        self.queue[parent], self.queue[last] = self.queue[last], self.queue[parent]


    def insert(self, val):
        # 맨 마지막에 삽입할 원소를 추가
        self.queue.append(val)
        last_idx = len(self.queue)-1
        while 0 <= last_idx:
            parent_idx = self.parent(last_idx)
            if parent_idx >= 0 and self.queue[parent_idx] < self.queue[last_idx]:
                self.swap(last_idx, parent_idx)
                last_idx = parent_idx
            else:
                break

    def delete(self):
        last_idx = len(self.queue)-1
        if last_idx < 0:
            return -1

        self.swap(0, last_idx)
        val = self.queue.pop()
        self.heapify(0)

        return val

    def heapify(self, idx):

        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)
        max_idx = idx

        if left_idx <= len(self.queue)-1 and self.queue[max_idx] < self.queue[left_idx]:
            max_idx = left_idx
        if right_idx <= len(self.queue)-1 and self.queue[max_idx] < self.queue[right_idx]:
            max_idx = right_idx

        if max_idx != idx: # swap 되어야 하는 경우
            self.swap(idx, max_idx)
            self.heapify(max_idx)




heap = MaxHeap()
heap.insert(3)
heap.insert(5)
heap.insert(2)
heap.insert(7)
heap.insert(8)
heap.insert(9)
heap.insert(1)
heap.insert(10)
print(heap.queue)
sorted_list = []
print(heap.delete())
print(heap.queue)
print(heap.delete())
print(heap.heap_sort())