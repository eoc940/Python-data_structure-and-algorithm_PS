# 카펫

import math

def solution(brown, yellow):
    answer = []
    match = []
    for sero in range(1, int(math.sqrt(yellow)+1)):
        garo = yellow / sero
        if garo == int(garo):
            match.append([int(garo), sero])
    for ga, se in match:
        if brown+4 == 2*(ga+2) + 2*(se+2):
            return [ga+2, se+2]