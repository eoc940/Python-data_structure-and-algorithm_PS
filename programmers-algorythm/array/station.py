# 기지국 설치

import math

def solution(n, stations, w):
    answer = 0
    location = 1
    for station in stations:
        start, end = station-w, station+w
        distance = start - location
        if distance >= 0:
            answer += math.ceil(distance/(2*w+1))
        location = end + 1

    if location <= n:
        answer += math.ceil((n+1-location)/(2 * w + 1))

    return answer

n = 11
stations = [1,2,3,9]
w = 1
print(solution(n, stations, w))






