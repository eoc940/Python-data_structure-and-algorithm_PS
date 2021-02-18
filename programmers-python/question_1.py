# 몫과 나머지

a,b = map(int, input().split())
mok = a//b
nam = a%b
print(mok, nam)

# 강사님 풀이
a,b = map(int, input().split())
print(*divmod(a,b))

'''
divmod
무조건 divmod를 쓰는 게 좋은 건 아님
가독성이나 팀의 스타일에 따라 a//b, a%b와 같이 쓸 때가 더 좋을 수 있음
또한 divmod는 작은 수를다룰 때는 a//b, a%b보다 느림
그러나 큰 숫자를 다룰 때는 더 빠름
'''