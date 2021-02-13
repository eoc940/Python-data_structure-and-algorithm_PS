'''
문자열과 내장함수
'''
msg="It is Time"
print(msg.upper()) # 원본은 그대로고 대문자화시킨 결과만 출력
print(msg)
print(msg.lower()) # 원본은 그대로고 소문자화시킨 결과만 출력

tmp=msg.upper()
print(tmp)
print(tmp.find("T")) # 첫 번째 매개변수만 찾음
print(tmp.count("T")) # 매개변수의 개수를 찾음
print(msg[:2]) # slice기능 : index 0-1까지 출력
print(msg[3:5]) # index 3-4까지 출력
print(len(msg)) # 총 길이를 출력(공백포함)

for i in range(len(msg)) :
    print(msg[i], end="")
print()

for x in msg : # 문자열 자체에서 반복문 돌리기 가능
    print(x, end="")
print()

for x in msg :
    if x.isupper() : # 대문자인지 알려주는 함수
        print(x, end="")
print()
for x in msg:
    if x.islower() :
        print(x, end="")
print()
for x in msg:
    if x.isalpha() : # 알파벳만 참, 공백을 거짓
        print(x, end="")
print()

tmp="AZ"
for x in tmp :
    print(ord(x)) # ord 는 아스키 넘버를 출력해줌

tmp="az"
for i in tmp :
    print(ord(i))

tmp=65
print(chr(tmp)) # chr 은 아스키 넘버에 대응되는 문자를 출력