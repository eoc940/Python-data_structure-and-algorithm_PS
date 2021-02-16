'''
def sort_list(li, s, e) :
    li = list(li)
    return_list = list()
    for i in range(s-1, e) :
        return_list.append(li[i])
    return_list.sort()
    return return_list

def index_value(li, k) :
    li = list(li)
    return li[k-1]

trial = int(input())
output_dict = dict()

for i in range(trial) :
    n, s, e, k = map(int, input().split())
    input_list = [int(x) for x in input().split()]

    sorted_list = sort_list(input_list, s, e)
    value = index_value(sorted_list, k)
    output_dict["#%d" %(i+1)] = value

for key, value in output_dict.items() :
    print(key, value)
'''


# 강사님 풀이

import sys
sys.stdin=open("in1.txt", "rt")

T = int(input())
for t in range(T) :
    n, s, e, k = map(int, input().split())
    input_list = list(map(int, input().split()))
    input_list=input_list[s-1:e]
    input_list.sort()
    print("#%d %d" %(t+1,input_list[k-1]))




