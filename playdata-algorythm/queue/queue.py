# 큐 구현

class Queue(list) :
    put = list.append

    def peek(self):
        return self[0]

    def get(self):
        return self.pop(0)

q = Queue()
q.put(1)
q.put(5)
q.put(10)
print(q)
print(q.peek())
q.get()
print(q)




