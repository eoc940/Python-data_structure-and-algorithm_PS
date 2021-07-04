# 보석 쇼핑

from collections import defaultdict

def solution(gems):
    answer = [float('-inf'),float('inf')]
    gem_catalog = set()
    for x in gems:
        gem_catalog.add(x)
    # print(gem_catalog)
    lp, rp = 0,0
    gem_cnt = defaultdict(int)
    gem_cnt[gems[0]] += 1
    while True:
        if len(gem_cnt.keys()) < len(gem_catalog):
            rp += 1
            if rp==len(gems):
                break
            gem_cnt[gems[rp]] += 1
        else :
            if rp-lp < answer[1]-answer[0]:
                answer = [lp+1,rp+1]
            gem_cnt[gems[lp]] -= 1

            if gem_cnt[gems[lp]]==0:
                gem_cnt.pop(gems[lp])
            lp += 1
        # print(lp,rp,gem_cnt)

    return answer

gems = ["AA", "AB", "AC", "AA", "AC"]
print(solution(gems))


'''
def calc(heap_list):
    _min, _max = float('inf'), float('-inf')
    for idx, name in heap_list:
        if idx < _min:
            _min = idx
        if idx > _max:
            _max = idx
    return [_min,_max]


def solution(gems):
    answer = []
    min_dist = float('inf')
    gem_location = defaultdict(deque)
    gem_range_min = []

    for idx, name in enumerate(gems):
        gem_location[name].append(idx+1)
    # print(gem_location)
    for key in gem_location.keys():
        val = gem_location[key].popleft()
        heapq.heappush(gem_range_min, (val,key))
    # print(gem_range_min)
    # print(gem_location)
    try :
        while True :
            li = calc(gem_range_min)
            # print(gem_location)
            # print(gem_range_min)
            # print(li)

            if li[1]-li[0] < min_dist :
                min_dist = li[1]-li[0]
                answer = li
            idx, name = heapq.heappop(gem_range_min)
            val = gem_location[name].popleft()
            heapq.heappush(gem_range_min, (val,name))
    except:
        # 여기서 최대 최소 뽑아서 리턴해주면 됨
        return answer

gems = ["DIA", "EMERALD","RUBY", "RUBY","SAPPHIRE", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA","RUBY"]
print(solution(gems))

# 1 4 5 8
# 2 3
# 6
# 7
#
# 1 2 6 7
# 4 2 6 7
# 4 3 6 7
'''