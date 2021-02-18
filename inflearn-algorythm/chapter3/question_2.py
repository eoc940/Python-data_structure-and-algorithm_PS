# 숫자만 추출

def get_number(x) :
    number = ""
    for i in x :
        try:
            int(i)
            number += i
        except :
            continue
    return int(number)

def yaksoo(x) :
    cnt = 0
    for i in range(1,x+1) :
        if x%i==0 :
            cnt += 1
    return cnt

n = input()
print(get_number(n))
print(yaksoo(get_number(n)))

# 강사님 풀이

s = input()
res = 0
for x in s:
    if x.isdecimal() : # isdecimal 은 0부터 9까지, isdigit은 숫자인지 아닌지
        res = res*10 + int(x) # 입력된 순서대로 숫자로 바꾸는 방법
print(res)

cnt = 0
for i in range(1, res+1) :
    if res%i == 0 :
        cnt += 1
print(cnt)
