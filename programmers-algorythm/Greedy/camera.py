# 단속카메라



def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    #print(routes)
    _min = sorted(routes)[0][0]
    camera = _min-1
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))




'''
for i in range(-20,15):
    a[i] += 1

for i in range(-10,5) :
    a[i] += 1

for i, v in a.items():
    print(i,v)
'''
