# 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    maps = []
    for i in range(rows):
        tmp_list = []
        for j in range(columns):
            tmp_list.append(columns*i + j+1)
        maps.append(tmp_list)



    for query in queries:
        process_query = [x-1 for x in query]
        row_st, col_st, row_en, col_en = process_query
        tmp = []
        # 우방향
        for i in range(col_st, col_en):
            tmp.append(maps[row_st][i])
        # 아래방향
        for i in range(row_st, row_en):
            tmp.append(maps[i][col_en])
        # 좌방향
        for i in range(col_en, col_st, -1):
            tmp.append(maps[row_en][i])
        # 위방향
        for i in range(row_en, row_st, -1):
            tmp.append(maps[i][col_st])
        number = tmp.pop()
        tmp.insert(0, number)

        idx = 0
        # 우방향
        for i in range(col_st, col_en):
            maps[row_st][i] = tmp[idx]
            idx += 1
        # 아래방향
        for i in range(row_st, row_en):
            maps[i][col_en] = tmp[idx]
            idx += 1
        # 좌방향
        for i in range(col_en, col_st, -1):
            maps[row_en][i] = tmp[idx]
            idx += 1
        # 위방향
        for i in range(row_en, row_st, -1):
            maps[i][col_st] = tmp[idx]
            idx += 1
        answer.append(min(tmp))

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))