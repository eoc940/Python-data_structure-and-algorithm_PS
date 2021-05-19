# 카드 역배치

import sys

# 이따 마지막에 0번 인덱스 빼주기
cards = [x for x in range(21)]

for _ in range(10) :
    std, end = map(int, sys.stdin.readline().split())
    slice_list = cards[std : end+1]

    revert_list = slice_list[::-1]

    for i in range(end-std+1) :
        cards[std+i] = revert_list[i]
    #print(cards)

del cards[0]
for x in cards :
    print(x, end=" ")



