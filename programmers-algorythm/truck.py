# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    bridge_truck = []
    pass_truck = []
    time= 1
    while(len(pass_truck)<n) :
        time += 1
        if bridge_truck and truck_weights :
            total = 0

            for i in range(len(bridge_truck)) :
                total += bridge_truck[i][0]

            if total + truck_weights[0] <= weight :
                bridge_truck.append([truck_weights[0],0])
                truck_weights.pop(0)

        elif truck_weights :
            bridge_truck.append([truck_weights[0],0])
            truck_weights.pop(0)

        for j in range(len(bridge_truck)) :
            bridge_truck[j][1] += 1

        if bridge_truck[0][1] == bridge_length:
            pass_truck.append(bridge_truck[j][0])
            bridge_truck.pop(0)

    return time

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))


