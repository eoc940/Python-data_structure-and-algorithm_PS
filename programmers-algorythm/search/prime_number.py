# 소수 찾기

def decide_prime_num(number) :
    if number in [0,1] :
        return False
    elif number in [2,3] :
        return True
    elif number>=4 :
        for i in range(2, number//2+1) :
            if number%i == 0 :
                return False
        return True

def permutation(arr, count) :
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    num_set = set()
    def generage(chosen, used) :
        if len(chosen)==count :
            num = int(''.join(map(str, chosen)))
            num_set.add(num)
            return
        for i in range(len(arr)) :
            if not used[i] : #used[i]==0
                chosen.append(arr[i])
                used[i] = 1
                generage(chosen, used)
                used[i] = 0
                chosen.pop()
    generage([], used)
    return num_set

def solution(numbers):
    num_list = [int(numbers[x]) for x in range(len(numbers))]
    cnt = 0
    final_set = set()
    for i in range(1,len(num_list)+1) :
        num_set = permutation(num_list, i)
        num_set = list(num_set)
        for j in range(len(num_set)) :
            final_set.add(num_set[j])
    final_set = list(final_set)
    for k in range(len(final_set)) :
        if decide_prime_num(final_set[k]) :
            cnt += 1
    return cnt

print(solution("17"))
print(solution("011"))
