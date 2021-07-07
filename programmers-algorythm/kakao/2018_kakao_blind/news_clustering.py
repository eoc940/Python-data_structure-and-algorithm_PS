# 뉴스 클러스터링
import copy

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    list_one = []
    list_two = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha(): # 문자열 전체가 알파벳으로 구성되어 있는지 알려줌
            list_one.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            list_two.append(str2[i:i+2])
    # print(list_one)
    # print(list_two)
    if not list_one and not list_two: return 65536
    cnt = 0
    ch_one = [0]*len(list_one)
    ch_two = [0]*len(list_two)
    for i,v1 in enumerate(list_one):
        for j,v2 in enumerate(list_two):
            if v1==v2 and ch_one[i]==0 and ch_two[j]==0:
                ch_one[i]=1
                ch_two[j]=1
                break
    hap = len(ch_one) + len(ch_two) - sum(ch_one)
    kyo = sum(ch_one)

    return int(kyo/hap*65536)

str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(solution(str1,str2))

