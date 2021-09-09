# 방문 길이

def solution(dirs):
    answer = 0
    ch_route = dict()
    direction = {"U":(0,1), "D":(0,-1), "R":(1,0), "L":(-1,0)}
    x, y = 0, 0
    for direct in dirs:
        dx, dy = direction[direct]
        if -5<=x+dx<=5:
            x += dx
        else:
            continue
        if -5<=y+dy<=5:
            y += dy
        else:
            continue

        try:
            if ch_route[(x-dx, y-dy, x, y)]==1 or ch_route[(x, y, x-dx, y-dy)]==1:
                # print("##@@##")
                continue
        except: # 해당 길 방문 안했을때
            ch_route[(x - dx, y - dy, x, y)] = 1
            ch_route[(x, y, x - dx, y - dy)] = 1
            answer += 1
        # print(ch_route)
        # print()

    return answer

dirs = "ULURRDLLU"
print(solution(dirs))