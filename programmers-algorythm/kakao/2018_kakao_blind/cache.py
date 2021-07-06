# [1차] 캐시

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            answer += 1
            cache.append(city)
        else:
            if len(cache) != 0 and len(cache) == cacheSize:
                cache.popleft()
            if cacheSize != 0:
                cache.append(city)
            answer += 5
        # print(cache)

    return answer

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))

