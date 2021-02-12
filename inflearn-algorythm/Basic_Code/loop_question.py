# 1번. 1부터 N까지 홀수 출력하기
N = int(input("1.자연수를 입력하세요 : "))
for i in range(N+1) :
    if i%2==1 :
        print(i, end=" ")
print()

# 2번. 1부터 N까지의 합 구하기
N = int(input("2.자연수를 입력하세요 : "))
sum = 0
for i in range(N+1) :
    sum += i
print(sum)


# 3번. N의 약수출력하기
N = int(input("3.자연수를 입력하세요 : "))

for i in range(1,N+1) :
    if N%i==0 :
        print(i, end=" ")