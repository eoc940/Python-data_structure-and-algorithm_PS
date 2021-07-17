# n진수 게임

from collections import deque

def convert(num, n):
    mapping = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    stk = deque()
    if num==0:
        return '0'
    while num > 0 :
        stk.appendleft(mapping[num%n])
        num //= n
    return ''.join(stk)

def all_num_str(n,t,m):
    min_len = t*m
    num = 0
    result = ''
    while len(result) < min_len:
        result += convert(num, n)
        num += 1
    return result

def solution(n, t, m, p):
    answer = ''
    num_str = all_num_str(n,t,m)
    for i in range(t):
        answer += num_str[i*m + p-1]
    return answer

n,t,m,p = 16,16,2,2
print(solution(n,t,m,p))

