# 스도쿠

# 함수로 분리하고, 3*3 행렬 올바른지 체크하자

a = [list(map(int, input().split())) for _ in range(9)]

right = set([1,2,3,4,5,6,7,8,9])

def make_list(b, c) :
    tmp = set()
    for i in range(b,b+3) :
        for j in range(c,c+3) :
            tmp.add(a[i][j])
    return tmp


def check_square(a) :
    a = list(a)
    for i in range(0,9,3) :
        tmp = list()
        for j in range(0,9,3) :
            tmp = make_list(i,j)
            if right == tmp :
                continue
            else :
                return False
    return True

def check_column(a) :
    a = list(a)
    for i in range(len(a)) :
        tmp = set()
        for j in range(len(a)) :
            tmp.add(a[i][j])
        if right == tmp :
            continue
        else :
            return False
    return True

def check_row(a) :
    a = list(a)
    for i in range(len(a)) :
        tmp = set()
        for j in range(len(a)) :
            tmp.add(a[j][i])
        if right == tmp :
            continue
        else:
            return False
    return True
check_lists = [check_square(a), check_row(a), check_column(a)]
if all(check_lists) :
    print("YES")
else:
    print("NO")

# 스도쿠 검사

def check(a) :
    for i in range(9) :
        ch1 = [0]*10 # 행 체크
        ch2 = [0]*10 # 열 체크
        for j in range(9) :
            ch1[a[i][j]] = 1
            ch2[a[i][j]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9 :
            return False
    for i in range(3) :
        for j in range(3) :
            ch3 = [0]*10
            for k in range(3) :
                for s in range(3) :
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3) != 9 :
                return False
    return True



a = [list(map(int, input().split())) for _ in range(9)]
if check(a) :
    print("YES")
else :
    print("NO")


