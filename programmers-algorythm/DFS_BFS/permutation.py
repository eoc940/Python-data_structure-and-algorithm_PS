# permutation 구현하기

def permutation(arr, count) :
    arr = sorted(arr)
    ch = [0 for _ in range(len(arr))]
    answer = set()

    # generate에서 하나씩 뽑아서 answer에 넣어줄 것임
    def generate(chosen, check) :
        if len(chosen)==count :
            elem = ''.join(chosen)
            answer.add(elem)
            return
        for i in range(len(arr)):
            if check[i]==0 :
                chosen.append(arr[i])
                check[i] = 1
                generate(chosen, check)
                check[i] = 0
                chosen.pop()
    generate([], ch)
    return sorted(list(answer))

print(permutation(['a','b','c','d'],2))