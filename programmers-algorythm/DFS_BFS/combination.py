# 조합

def combination(arr, count) :
    arr = sorted(arr)
    ch = [0 for _ in range(len(arr))]
    answer = set()

    def generate(chosen, criteria_num) :
        if len(chosen)==count :
            elem = "".join(chosen)
            answer.add(elem)
            return
        for i in range(criteria_num,len(arr)) :
            chosen.append(arr[i])
            generate(chosen, criteria_num+1)
    generate([],0)
    return sorted(list(answer))


print(combination(['a','b','c','d'],2))