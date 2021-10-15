# n^2 배열 자르기

def solution(n, left, right):
    answer = []
    row_st, col_st = divmod(left,n)
    row_en, col_en = divmod(right,n)

    row = row_st
    col = col_st
    while True:

        answer.append(max(row, col) + 1)
        if col == n-1:
            row += 1
            col = 0
        else:
            col += 1

        if row == row_en and col == col_en:
            answer.append(max(row,col)+1)
            break

    return answer

n = 4
left = 7
right = 14
print(solution(n,left,right))
