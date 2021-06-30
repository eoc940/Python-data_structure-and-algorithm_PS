def b(li):
    for i in range(len(li)):
        li[i] -= 1
def a(li):
    b(li)
    b(li)
    return li

li = [1,2,3]
print(a(li))