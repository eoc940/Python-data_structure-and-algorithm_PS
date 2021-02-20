# 문자열 정렬하기

def print_string(s, n) :
    s_len = len(s)
    interval = int((n-s_len)/2)
    print(s)
    print(" "*interval, s, sep="")
    print(" "*interval*2, s, sep="")

s, n = input().split()
n = int(n)
print_string(s, n)

# 강사님 풀이

s = 'abcd'
n = 7
s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬