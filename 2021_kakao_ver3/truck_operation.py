import requests
import json
from truck_class import truck
import random

# API

token = '694673e628d83ed45979e87671de0108'
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

def move_one(tr, locations):
    _truck = truck(tr["id"], tr["location_id"], tr["loaded_bikes_count"], MAX_LENG, [])
    command = []
    max_place = []
    min_place = []
    for i in range(MAX_LENG):
        for j in range(MAX_LENG):
            max_place.append((locations[i][j],i,j))
            min_place.append((locations[i][j], i, j))
    max_place.sort(key=lambda x : x[0], reverse=True)
    min_place.sort(key=lambda x : x[0])

    if _truck.bike > 0: # 가지고 있다면 없는 곳으로 간다
        bike_cnt, row, col = min_place[_truck.tid]
        # 1,3 -> 3,4
        up = _truck.row - row
        left = _truck.col - col
        if up > 0:
            for _ in range(up):
                _truck.up()
        else:
            for _ in range(-up):
                _truck.down()
        if left > 0:
            for _ in range(left):
                _truck.left()
        else:
            for _ in range(-left):
                _truck.right()
        for _ in range(_truck.bike):
            _truck.land()
            locations[row][col] += 1

    else: # 최대 많은 곳으로 가서 싣고 없는 곳으로 간다
        bike_cnt, row, col = max_place[_truck.tid]
        # 1,3 -> 3,4
        up = _truck.row - row
        left = _truck.col - col
        if up > 0:
            for _ in range(up):
                _truck.up()
        else:
            for _ in range(-up):
                _truck.down()
        if left > 0:
            for _ in range(left):
                _truck.left()
        else:
            for _ in range(-left):
                _truck.right()
        if locations[_truck.row][_truck.col] >= AVG_BIKE:
            load_cnt = locations[_truck.row][_truck.col] + 1 - AVG_BIKE
            for _ in range(load_cnt):
                _truck.load()
                locations[row][col] -= 1

        bike_cnt, row, col = min_place[_truck.tid]
        # 1,3 -> 3,4
        up = _truck.row - row
        left = _truck.col - col
        if up > 0:
            for _ in range(up):
                _truck.up()
        else:
            for _ in range(-up):
                _truck.down()
        if left > 0:
            for _ in range(left):
                _truck.left()
        else:
            for _ in range(-left):
                _truck.right()
        for _ in range(_truck.bike):
            _truck.land()
            locations[row][col] += 1


    print("command :", _truck.command)
    return {"truck_id":_truck.tid, "command":_truck.command[:10]}

def move_two(tr, locations):
    _truck = truck(tr["id"], tr["location_id"], tr["loaded_bikes_count"], MAX_LENG, [])
    command = []
    # print(locations)


    print("command :", command)
    return {"truck_id":_truck.tid, "command":command[:10]}

# 시나리오 1

MAX_LENG = 5
AVG_BIKE = 4
auth_key = startAPI(1)

while True:
    location_json = locationAPI(auth_key)
    locations = convert(location_json)
    print(locations)
    check = [[False for _ in range(MAX_LENG)] for _ in range(MAX_LENG)]
    trucks = truckAPI(auth_key)
    commands = []
    for tr in trucks:
        truck_action = move_one(tr, locations)
        commands.append(truck_action)
    status, time, fail_count, distance = simulateAPI(auth_key, commands)
    print("time :", time)
    print("fail :", fail_count)
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
#         truck_action = move_two(tr, locations)
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
