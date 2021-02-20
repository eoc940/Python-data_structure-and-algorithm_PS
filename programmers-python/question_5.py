# 2차원 리스트 뒤집기

def solution(mylist) :
    return_list = list()
    index_num = 0
    for i in range(len(mylist)) :
        tmp_list = list()
        for j in range(len(mylist)) :
            tmp_list.append(mylist[j][i])
        return_list.append(tmp_list)
    return return_list

my = [[1,2,3],[4,5,6],[7,8,9]]
print(solution(my))

# 강사님 풀이

mylist = [[1,2,3], [4,5,6], [7,8,9]]
new_list = list(map(list, zip(*mylist)))

'''
zip을 사용하면 리스트들의 index 맞는 것끼리 묶임
'''

mylist = [1,2,3]
new_list = [40,50,60]
for i in zip(mylist, new_list) :
    print(i)
'''
출력결과
(1,40)
(2,50)
(3,60)
'''
