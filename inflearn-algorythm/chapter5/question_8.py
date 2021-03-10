# 단어 찾기(해쉬)

n = int(input())

words = [input() for _ in range(n)]
miss_words = [input() for _ in range(n-1)]
words.sort()
miss_words.sort()

for i in range(n-1) :
    if words[i] != miss_words[i] :
        print(words[i])
        break
else:
    print(words[n-1])

# 강사님 풀이

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word]=0
for key, value in p.items():
    if value == 1 :
        print(key)






