# 스택 구현
# 1
'''
class Stack(list) :

    push = list.append

    def peek(self):
        return self[-1]

s = Stack()
s.push(1)
s.push(5)
s.push(10)
print(s)
print(s.peek())
print(s)
s.pop()
print(s)
'''

# 2
s = []
s.append(1)
s.append(5)
s.append(10)
print(s)
s.pop()
print(s)
print(s[-1])



