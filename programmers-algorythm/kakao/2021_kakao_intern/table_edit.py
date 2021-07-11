# 표 편집

def solution(n, k, cmd):
    answer = ''
    table = [x for x in range(n)]
    deleted = []
    idx = k
    for command in cmd :
        com = command.split()

        if com[0] == "D":
            idx += int(com[1])
        elif com[0] == "U":
            idx -= int(com[1])
        elif com[0] == "C":
            deleted.append(table[idx])
            if idx==table[-1]:
                idx -= 1
            table.pop()
        elif com[0] == "Z":
            reset = deleted.pop()
            if reset <= idx :
                idx += 1
            table.append(table[-1] + 1)
        print(com)
        print(idx)
        print(table)
        print(deleted)
        print()
    # print(deleted)

    for i in range(n):
        if i in deleted:
            answer += 'X'
        else:
            answer += 'O'

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n,k,cmd))