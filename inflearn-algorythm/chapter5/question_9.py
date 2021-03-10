# 아나그램

first = input()
second = input()
first_dic = dict()
second_dic = dict()

for i in range(len(first)) :
    if first[i] in first_dic:
        first_dic[first[i]] += 1
    else:
        first_dic[first[i]] = 0

for i in range(len(second)) :
    if second[i] in second_dic:
        second_dic[second[i]] += 1
    else:
        second_dic[second[i]] = 0

if first_dic == second_dic :
    print("YES")
else :
    print("NO")

# 강사님 풀이

a = input()
b = input()
str1 = dict()
str2 = dict()

for x in a :
    # .get을 이용하여 키에 x가 없으면 0을 리턴하고
    # 키에 x가 있으면 value를 리턴한다
    str1[x] = str1.get(x, 0)+1
for x in b :
    str2[x] = str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

# 다른 풀이

a = input()
b = input()
sH = dict()
for x in a :
    sH[x] = sH.get(x, 0) + 1
for x in b :
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break

else:
    print("YES")