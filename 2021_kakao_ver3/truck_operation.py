import requests
import json
from truck_class import truck
import random

# API

token = '356384a925546199b8a9c8cce5d0af5a'
url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'

def startAPI(problem):
    headers = {
        'X-Auth-Token':token,
        'Content-Type':'application/json'
    }
    data = json.dumps({"problem":problem})
    response = requests.post(url + '/start', headers=headers, data=data)
    auth_data = response.json()
    auth_key = auth_data["auth_key"]
    return auth_key

def locationAPI(auth_key):
    headers = {
        'Authorization':auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url + '/locations', headers=headers)
    location_data = response.json()
    return location_data["locations"]

def truckAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url + '/trucks', headers=headers)
    truck_data = response.json()
    return truck_data["trucks"]

def simulateAPI(auth_key, commands):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"commands":commands})
    response = requests.put(url + '/simulate', headers=headers, data=data)
    simulate_data = response.json()
    status = simulate_data["status"]
    time = simulate_data["time"]
    fail_count = simulate_data["failed_requests_count"]
    distance = simulate_data["distance"]
    return status, time, fail_count, distance

def scoreAPI(auth_key):
    headers = {
        'Authorization': auth_key,
        'Content-Type': 'application/json'
    }
    response = requests.get(url + '/score', headers=headers)
    score_data = response.json()
    score = score_data["score"]
    return score

# function

def convert(location_json):
    locations = [[0 for _ in range(MAX_LENG)] for _ in range(MAX_LENG)]
    for location in location_json:
        x,y = divmod(location["id"],MAX_LENG)
        locations[MAX_LENG-1-y][x] = location["located_bikes_count"]
    return locations

def move(tr, locations):
    _truck = truck(tr["id"], tr["location_id"], tr["loaded_bikes_count"], MAX_LENG)
    command = []

    near = [_truck.row, _truck.col]
    max_dist = 0
    # 가장 먼 부족한 곳 탐색
    # print("location :", locations)
    for i in range(MAX_LENG):
        for j in range(MAX_LENG):
            if locations[i][j] < AVG_BIKE and not check[i][j]:
                dist = abs(_truck.row - i) + abs(_truck.col - j)
                if max_dist < dist and dist <= 6 and [i,j] != [_truck.row, _truck.col]:
                    max_dist = dist
                    near = [i, j]
                    check[i][j] = True

    # 거리 8 이내의 가장 먼 곳이 탐색됨
    down = near[0] - _truck.row
    right = near[1] - _truck.col
    move_list = []
    if down > 0:
        for _ in range(down):
            move_list.append("down")
    else: # up
        for _ in range(-down):
            move_list.append("up")
    if right > 0:
        for _ in range(right):
            move_list.append("right")
    else: # left
        for _ in range(-right):
            move_list.append("left")

    random.shuffle(move_list)
    print([_truck.row, _truck.col],near, locations[near[0]][near[1]],move_list)
    command = []
    if locations[_truck.row][_truck.col] >= AVG_BIKE:
        command.append(_truck.load())
        locations[_truck.row][_truck.col] -= 1
    elif locations[_truck.row][_truck.col] < AVG_BIKE-1:
        command.append(_truck.land())
        locations[_truck.row][_truck.col] += 1
    for mv in move_list:
        if mv=="up":
            command.append(_truck.up())
        elif mv=="down":
            command.append(_truck.down())
        elif mv=="left":
            command.append(_truck.left())
        elif mv=="right":
            command.append(_truck.right())
        if locations[_truck.row][_truck.col] >= AVG_BIKE:
            command.append(_truck.load())
            locations[_truck.row][_truck.col] -= 1
        elif locations[_truck.row][_truck.col] < AVG_BIKE - 1:
            command.append(_truck.land())
            locations[_truck.row][_truck.col] += 1

    if len(command) == 0:
        if locations[_truck.row][_truck.col] >= AVG_BIKE:
            command.append(_truck.load())
            locations[_truck.row][_truck.col] -= 1
        elif locations[_truck.row][_truck.col] < AVG_BIKE - 1:
            command.append(_truck.land())
            locations[_truck.row][_truck.col] += 1
        for i in range(6):
            num = random.randrange(1,5)
            if num==1:
                command.append(_truck.up())
            elif num==2:
                command.append(_truck.down())
            elif num==3:
                command.append(_truck.left())
            else: # 4
                command.append(_truck.right())
            if locations[_truck.row][_truck.col] >= AVG_BIKE:
                command.append(_truck.load())
                locations[_truck.row][_truck.col] -= 1
            elif locations[_truck.row][_truck.col] < AVG_BIKE - 1:
                command.append(_truck.land())
                locations[_truck.row][_truck.col] += 1

    removed_none = []
    for com in command:
        if com != None: removed_none.append(com)

    command = removed_none
    # print("command :", command[:10])

    return {"truck_id":_truck.tid, "command":command[:10]}


# 시나리오 1

MAX_LENG = 5
AVG_BIKE = 4
auth_key = startAPI(1)

while True:
    location_json = locationAPI(auth_key)
    locations = convert(location_json)
    check = [[False for _ in range(MAX_LENG)] for _ in range(MAX_LENG)]
    trucks = truckAPI(auth_key)
    commands = []
    for tr in trucks:
        truck_action = move(tr, locations)
        commands.append(truck_action)
    status, time, fail_count, distance = simulateAPI(auth_key, commands)
    print("time :", time)
    if status == "finished":
        print("실패 :", fail_count)
        print("디폴트 성공률 :", 1077, "/", 1428)
        print("나의  성공률 :", 1428-int(float(fail_count)), "/", 1428)
        break

print(scoreAPI(auth_key))

# 시나리오 2

# MAX_LENG = 60
# AVG_BIKE = 3
# auth_key = startAPI(2)
#
# while True:
#     location_json = locationAPI(auth_key)
#     locations = convert(location_json)
#     check = [[False for _ in range(MAX_LENG)] for _ in range(MAX_LENG)]
#     trucks = truckAPI(auth_key)
#     commands = []
#     for tr in trucks:
#         truck_action = move(tr, locations)
#         commands.append(truck_action)
#     status, time, fail_count, distance = simulateAPI(auth_key, commands)
#     print("time :", time)
#     if status == "finished":
#         print("실패 :", fail_count)
#         print("디폴트 성공률 :", 9142, "/", 10829)
#         print("나의  성공률 :", 10829-int(float(fail_count)), "/", 10829)
#         break
#
# print(scoreAPI(auth_key))
