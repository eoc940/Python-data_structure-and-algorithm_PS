# 차이를 최대로

import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))

candi = []


possi_list = []
def permutation(arr,r):
    arr.sort()
    ch = [0]*len(arr)

    def generate(chosen, ch):
        if len(chosen)==r:
            possi_list.append(tuple(chosen))
            return
        for i in range(len(arr)):
            if not ch[i]: # ch[i] == 0일 경우
                chosen.append(arr[i])
                ch[i] = 1
                generate(chosen, ch)
                ch[i] = 0
                chosen.pop()
    generate([],ch)

permutation(nums, n)
answer = float('-inf')
for li in possi_list:
    tmp = 0
    for i in range(len(li)-1):
        tmp += abs(li[i]-li[i+1])
    answer = max(answer, tmp)
print(answer)


