

def solution(n, k, cmd):
    answer = ''
    row = [x for x in range(n)]
    stk = []

    focus = k
    for i in cmd :

        if i=="C" :
            stk.append(row[focus])
            del row[focus]
            if focus == len(row) :
                focus -= 1

        elif i=="Z" :
            reset_num = stk.pop()
            row.insert(reset_num, reset_num)
            if reset_num <= focus :
                focus += 1
        else :
            command, num = i.split(" ")
            num = int(num)
            if command=="U" :
                focus -= num
            elif command=="D" :
                focus += num
        print(i," focus :",focus," row :", row, " stk :",stk)

    for j in range(n) :
        if j in row :
            answer += "O"
        else :
            answer += "X"

    return answer

print(solution(8,2,["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C", "C"]))