# 회문 문자열 검사

def check_str(x) :
    x = x.upper()
    for i in range(len(x)) :
        if x[i] == x[len(x)-i-1] :
            continue
        else:
            return False
    return True

n = int(input())
for i in range(n) :
    word = input()
    if check_str(word) :
        print("#%d" %(i+1), "YES")
    else :
        print("#%d" %(i+1), "NO")

# 강사님 풀이

n = int(input())
for i in range(n) :
    s=input().upper()
    size=len(s)
    for j in range(size//2):
        if s[j] != s[-1-j] : # 음수 인덱스 활용
            print("#%d NO" %(i+1))
            break
    else:
        print("%%d YES" %(i+1))

# 더 짧은 풀이

n = int(input())
for i in range(n) :
    s=input().upper()
    if s == s[::-1] : # 문자열을 거꾸로 하는 슬라이싱
        print("%%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))