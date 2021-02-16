# 뒤집은 소수
'''
def reverse(x) :
    string = ""
    while x > 0 :
        string += str(x%10)
        x = int(x/10)
    string = int(string)
    return string

def isPrime(x) :
    cnt = 0
    for i in range(1,x+1) :
        if x%i == 0 :
            cnt+=1
    if cnt == 2 :
        return True
    else:
        return False


n = int(input())
num_list = list(map(int, input().split()))
reverse_list = list()
for i in range(len(num_list)) :
    reverse_list.append(reverse(num_list[i]))

for i in reverse_list :
    if isPrime(i) :
        print(i, end=" ")
'''
# 강사님 풀이

n = int(input())
a = list(map(int, input().split()))

def reverse(x) :
    res = 0
    while x>0 :
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x) :
    if x==1 :
        return False
    for i in range(2, x//2+1) :
        if x%i==0:
            return False
    return True

for x in a :
    tmp = reverse(x)
    if isPrime(tmp) :
        print(tmp, end=" ")



