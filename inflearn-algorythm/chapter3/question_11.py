# 격자판 회문수

a = [list(map(int, input().split())) for _ in range(7)]


# 이거 말고 tmp == tmp[::-1] 쓰면 한줄이면 된다.
def check_num(a) :
    mid = len(a)//2
    for i in range(mid) :
        if a[i] != a[-i-1] :
            return False
    return True
cnt = 0
# 3중, 4중 for문 쓰는 거 두려워하지말자. 2개씩 끊어서 보거나 하면
# 의미를 읽을 수 있다.
for i in range(7) :
    for j in range(3) :
        tmp = list()
        tmp_row = list()
        for k in range(5) :
            tmp.append(a[i][j+k])
            tmp_row.append(a[j+k][i])
        if check_num(tmp) :
            cnt += 1
        if check_num(tmp_row) :
            cnt += 1

print(cnt)

# 강사님 풀이

a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3) :
    for j in range(7) :
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1] :
            cnt += 1
        for k in range(2) : # 세로 회문 검사
            if a[i+k][j] != a[i+5-k-1][j] :
                break
        else:
            cnt += 1

print(cnt)