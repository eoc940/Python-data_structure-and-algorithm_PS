# n진수 게임

def convert(num, n, num_dict):
    num_list = list()
    if num == 0: return '0'
    while num > 0:
        num_list.append(num%n)
        num //= n
    string = ''
    for i in range(len(num_list)-1,-1,-1):
        string += num_dict[num_list[i]]
    return string

def solution(n, t, m, p):
    answer = ''
    num_dict = dict()
    for i in range(10):
        num_dict[i] = str(i)
    for i in range(6):
        num_dict[i+10] = chr(i+65)

    # t*m만큼의 문자열을 구해놓고 m,p를 이용해서 알맞은 것을 빼내서 answer에 더하자
    num = 0
    string = ''
    while len(string) < t*m:
        string += convert(num, n, num_dict)
        num += 1

    mul = 0
    for _ in range(t):
        answer += string[p-1 + m*mul]
        mul += 1

    return answer

n,t,m,p = 16,16,2,2
print(solution(n,t,m,p))
