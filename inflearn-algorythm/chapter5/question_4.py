# 후위식 연산

n = input()
stack = []

for i in range(len(n)) :

    if n[i]=="+":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1+n2)
    elif n[i]=="-":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 - n1)
    elif n[i]=="*":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n1 * n2)
    elif n[i]=="/":
        n1 = stack.pop()
        n2 = stack.pop()
        stack.append(n2 / n1)
    else :
        stack.append(int(n[i]))

print(stack.pop())

# 강사님 풀이

a = input()
stack = []
for x in a:
    if x.isdecimal() :
        stack.append(int(x))
    else:
        if x=="+" :
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x=="-":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x=="*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == "/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)

print(stack.pop())